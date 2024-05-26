class Atm:

    #functions and methods
    #constructor
    #special/magic/dunder methods
    #instance variable
    #reference variable ---> sbi = Atm()
    #static or class variable

    __counter = 1     #static variable is same for all objects of that class
    
    def __init__(self):

        self.__pin = ""     #private attributes
        self.__balance = 0  #private attributes  but can be get by using sbi._Atm__balance

        self.sno = Atm.get_counter()
        Atm.__counter = Atm.__counter + 1
        
        print(id(self))

        self.__menu()

    @staticmethod
    def get_counter():
        return Atm.__counter

    @staticmethod
    def set_counter(new):
        if type(new) ==  int:
            Atm.__counter = new
        else:
            print("Not allowed")

    def get_pin(self):
        return self.__pin

    def set_pin(self, new_pin):
        if type(new_pin) ==str:
            self.__pin = new_pin
            print("Pin changed")
        else:
            print("Not allowed")

    def __menu(self):
        user_input = input("""
                        Hello, how would you like to proceed?
                        1. Enter 1 to create pin
                        2. Enter 2 to deposit
                        3. Enter 3 to withdraw
                        4. Enter 4 to check balance
                        5. Enter 5 to exit

""")
        if user_input == "1":
            self.create_pin()
        elif user_input == "2":
            self.deposit()
        elif user_input == "3":
            self.withdraw()
        elif user_input == "4":
            self.check_balance()
        else:
            print("bye")

    def create_pin(self):
        self.__pin = input("Enter you Pin: ")
        print("Pin set successfully")

    def deposit(self):
        temp = input("Enter your pin: ")
        if temp == self.__pin:
            amount = int(input("Enter the amount: "))
            self.__balance = self.__balance + amount
            print("Deposit successfully")
        else:
            print("Invalid pin")

    def withdraw(self):
        temp = input("Enter your pin: ")
        if temp == self.__pin:
            amount = int(input("Enter the amount: "))
            if amount < self.__balance:
                self.__balance = self.__balance - amount
                print("Operation successfully")
            else:
                print("Insufficient funds")
        else:
            print("Invalid pin")
            
    def check_balance(self):
        temp = input("Enter your pin: ")
        if temp == self.__pin:
            print(self.__balance)
        else:
            print("Invalid pin")
    
