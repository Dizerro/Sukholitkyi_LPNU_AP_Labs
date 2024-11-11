from enum import Enum

class CandyType(Enum):

    Bar = 1
    Button = 2
    Popcorn = 3 
    Gum = 4 

class Candy:

    def __init__(self, name = None, mass_in_grams = None, amount = None, price = None, candy_type = None):
        self.__name = name
        self.__mass_in_grams = mass_in_grams
        self.__amount = amount
        self.__price = price
        self.__candy_type = candy_type

    def get_name(self):
        return self.__name

    def get_mass_in_grams(self):
        return self.__mass_in_grams

    def get_amount(self):
        return self.__amount
    
    def get_price(self):
        return self.__price
    
    def get_candy_type(self):
        return self.__candy_type
    
    def __del__(self):
        print(f"{self.__name} -> deleted")

    def ate(self):
        total_mass = self.__mass_in_grams * self.__amount
        if total_mass > 2000:
            return "You are on a diet!"
        else:
            return "What delicious candies!"
        
    def display_info(self):
        print (f"Name:{self.__name}, {self.__mass_in_grams} grams, {self.__amount} sweets, {self.__price} USD, {self.__candy_type.name}")
    
    def setattr_amount(self, adding_sweets):
        self.__amount = self.__amount + adding_sweets

class Dinner:
    def __init__(self, day = None, time = None, candies = None):
        self.__day = day
        self.__time = time
        self.__candies = candies

    def findTheMostExpensiveCandies(self):
        sorted_candies = sorted(self.__candies, key=lambda candy: candy.get_price(), reverse=True)
        top_3 = sorted_candies[:3]
        return top_3

    
    def display_dinner_info(self):
            print(f"Dinner on {self.__day} at {self.__time}")
            for candy in self.__candies:
                candy.display_info()

def main():

    candy_1 = Candy("Snickers", 50, 10, 2.5,CandyType.Bar)
    candy_2 = Candy("M&M's", 10, 50, 1.0, CandyType.Button)
    candy_3 = Candy("Popcorn Caramel", 100, 5, 3.5, CandyType.Popcorn)
    candy_4 = Candy("Orbit", 5, 20, 0.5, CandyType.Gum)
    candy_5 = Candy("Mars", 60, 15, 3.0, CandyType.Bar)

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

main()