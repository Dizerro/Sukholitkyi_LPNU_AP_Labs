from enum import Enum

class CandyType(Enum):

    Bar = 1
    Button = 2
    Popcorn = 3 
    Gum = 4 

class Candy:

    def __init__(self, name = None, mass_in_grams = None, amount = None, price = None, calories = None,candy_type = None):
        self.__name = name
        self.__mass_in_grams = mass_in_grams
        self.__amount = amount
        self.__price = price
        self.__calories = calories
        self.__candy_type = candy_type

    def get_name(self):
        return self.__name

    def get_mass_in_grams(self):
        return self.__mass_in_grams

    def get_amount(self):
        return self.__amount
    
    def get_price(self):
        return self.__price

    def get_calories(self):
        return self.__calories
    
    def get_candy_type(self):
        return self.__candy_type
    
    #def __del__(self):
    #    print(f"{self.__name} -> deleted")

    def ate(self):
        total_mass = self.__mass_in_grams * self.__amount
        if total_mass > 2000:
            return "You are on a diet!"
        else:
            return "What delicious candies!"
        
    def display_info(self):
        print (f"Name:{self.__name}, {self.__mass_in_grams} grams, {self.__amount} sweets, {self.__price} USD, {self.__calories} calories, {self.__candy_type.name}")
    
    def setattr_amount(self, adding_sweets):
        self.__amount = self.__amount + adding_sweets

class Dinner:
    def __init__(self, day = None, time = None, candies = None):
        self.__day = day
        self.__time = time
        self.__candies = candies

    def get_candies(self):
        return self.__candies

    def findTheMostExpensiveCandies(self):
        top_3 = []
        for i in range(3):
            max_price = -1
            max_candy = None
            for candy in self.__candies:
                if candy.get_price() > max_price and candy not in top_3:
                    max_price = candy.get_price()
                    max_candy = candy
            if max_candy:
                top_3.append(max_candy)
        return top_3
    
    def display_dinner_info(self):
            print(f"Dinner on {self.__day} at {self.__time}")
            for candy in self.__candies:
                candy.display_info()

class Store:

    def __init__(self, dinners = None):
        self.__dinners = dinners
    
    def find_best_dinner(self):
        best_dinner = None
        max_price = -1
        min_calories = float('inf')

        for dinner in self.__dinners:
            total_price = 0
            total_calories = 0

            for candy in dinner.get_candies():
                total_price += candy.get_price()
                total_calories += candy.get_calories()

            if total_price > max_price or (total_price == max_price and total_calories < min_calories):
                max_price = total_price
                min_calories = total_calories
                best_dinner = dinner

        return best_dinner

    def display_best_dinner(self):
        best_dinner = self.find_best_dinner()
        if best_dinner:
            print("\nBest dinner based on highest price and lowest calories:")
            best_dinner.display_dinner_info()
        else:
            print("No dinners available.")

def main():

    candy_1 = Candy("Snickers", 50, 10, 2.5, 300, CandyType.Bar)
    candy_2 = Candy("M&M's", 10, 50, 1.0, 230, CandyType.Button)
    candy_3 = Candy("Popcorn Caramel", 100, 5, 3.5, 250, CandyType.Popcorn)
    candy_4 = Candy("Orbit", 5, 20, 0.5, 50, CandyType.Gum)
    candy_5 = Candy("Mars", 60, 15, 3.0, 270, CandyType.Bar)
    candy_6 = Candy("Twix", 55, 12, 2.8, 280, CandyType.Bar)
    candy_7 = Candy("Skittles", 8, 40, 1.2, 200, CandyType.Button)
    candy_8 = Candy("Popcorn Butter", 120, 6, 4.0, 260, CandyType.Popcorn)
    candy_9 = Candy("Trident", 4, 25, 0.6, 40, CandyType.Gum)
    candy_10 = Candy("KitKat", 45, 18, 2.7, 250, CandyType.Bar)

    candy_2.setattr_amount(151)
    
    candy_1.display_info()
    print(candy_1.ate())
    
    candy_2.display_info()
    print(candy_2.ate())

    candies = [candy_1, candy_2, candy_3, candy_4, candy_5]
    dinner = Dinner("Monday", "18:00", candies)
    
    dinner.display_dinner_info()

    top_3_candies = dinner.findTheMostExpensiveCandies()
    print("\nTop 3 most expensive candies:")
    for candy in top_3_candies:
        candy.display_info()
    
    candies_1 = [candy_1, candy_2, candy_3, candy_4, candy_5]
    candies_2 = [candy_6, candy_7, candy_8, candy_9, candy_10]

    dinner_1 = Dinner("Monday", "18:00", candies_1)
    dinner_2 = Dinner("Tuesday", "19:00", candies_2)

    dinners = [dinner_1, dinner_2]
    store = Store(dinners)

    store.display_best_dinner()

main()