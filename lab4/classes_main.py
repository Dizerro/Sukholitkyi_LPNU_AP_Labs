class Pool:

    def __init__ (self, address = None, volume = None, maxpeople = None, enter_price = None, name = None):
        self.__address = address
        self.__volume = volume
        self.__maxpeople = maxpeople
        self.enter_price = enter_price
        self.name = name

    def get_adress(self):
        return self.__address
    
    def get_volume(self):
        return self.__volume
    
    def get_maxpeople(self):
        return self.__maxpeople
    
    def __str__(self):
         return f"Pool:{self.__address},{self.__maxpeople} persons,{self.__volume} liters"

    def __repr__(self):
        return (
        f"Басейн:\n"
        f"name = {self.name}\n"
        f"address = {self.__address}\n"
        f"enter_price = {self.enter_price}\n"
        f"volume = {self.__volume}\n"
        f"maxpeople = {self.__maxpeople}"
            )

    def __del__(self):
        print("deleted")

def main():
    Pool_1 = Pool()
    Pool_2 = Pool("Щирецька 36", 1000, 200, 500, "Три Стихії") 
    Pool_3 = Pool("Озерна 1", 750, 55 , 550, "KOI")

    print (repr(Pool_1))
    print (repr(Pool_2))
    print (repr(Pool_3))            

main()