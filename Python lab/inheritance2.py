class Phone:
    def __init__(self, price, brand, camera):

        print("Inside phone constructor")
        self.__price = price        #private data mem. cannot be inherited by another class
        self.brand = brand
        self.camera = camera

    def buy(self):
        print("Buying a phone")


class SmartPhone(Phone):

    def buy(self):
        print("Buying a smartphone")
        super().buy()

s = SmartPhone(2000, "apple", 13)

s.buy()


#method Overriding --> Polymorphism
#method Overloading ----> technically we can say overloading is not exit but we can achieve this by using default arguments
#Operator Overloading


# class Geometry:

#    def area(self, a, b=0):
#        if b==0:
 #           print("Cicle", 3.14*a*a)

 #      else:
#          print("Rect", a*b)

#obj=Geometry()
# obj.area(4)
#obj.area(4,5)
