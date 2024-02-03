#Types of variables in class =>
#1.Instance Variable = Varaibles which are use inside the for all oblects which will be changing the variable. 
#2.Class Variable = it is a varible which is defined outside the function and it will along with the classess, For all oblects which is used as common variable.

# EXAMPLES =
"""
class phone():
    chargertype="C-Type"
    def __init__(self,brand,price):
        self.brand=brand
        self.price=price
    def display(self):
        print("Brand : ",self.brand)
        print("Price : ",self.price)
        print("CharrgeType : ",self.chargertype)


samsung=phone("Samsung","60000")
samsung.display()

redmi=phone("Redmi","60000")
redmi.display()
    
OUTPUT :
Brand :  Samsung
Price :  60000
CharrgeType :  C-Type
Brand :  Redmi
Price :  60000
CharrgeType :  C-Type

#HERE chargertype="C-type" is a class variable
#self.brand=brand & self.price=price is instance variables
*******************************************************************
"""
#Types of Class Methods/Functions =>
"""
#Instance Method :

class laptop():
    chargertype="C-Type"
    def __init__(self):
        self.brand=""
        self.price=34
    def setPrice(self,price):
        self.price=price
    def getPrice(self):
        print(self.price)


hp=laptop()
hp.setPrice(20000)
hp.getPrice()

OUTPUT : 20000
*********************************************************************
"""
#Class Method :
"""
class laptop():
    chargertype="C-Type"
    def __init__(self):
        self.brand=""
        self.price=34
    def setPrice(self,price):
        self.price=price
    def getPrice(self):
        print(self.price)
    @classmethod
    def changeChargerType(cls):
        cls.chargertype="B-Type"
        print("Charger type changed to B")

hp=laptop()
hp.setPrice(20000)
hp.getPrice()

laptop.changeChargerType()

OUTPUT : 20000
         Charger type changed to B

#Here while calling the class output always we have to give an argument called (laptop),To avoid this we can use decrator.
#i.e above the class fuction  use @classmethod  and while calling the class output no need ot give an argument called (laptop)
************************************************************************
"""
#Static Method :
# where we wont use class and instance function but we have perform the output by function in this we can use Static Method

class laptop():
    chargertype="C-Type"
    def __init__(self):
        self.brand=""
        self.price=34
    def setPrice(self,price):
        self.price=price
    def getPrice(self):
        print(self.price)
    @classmethod
    def changeChargerType(cls):
        cls.chargertype="B-Type"
        print("Charger type changed to B")
    @staticmethod
    def info():
        print("This is laptop class")
hp=laptop()
hp.setPrice(20000)
hp.getPrice()

laptop.changeChargerType()
hp.info()

OUTPUT : 20000
         Charger type changed to B
         This is laptop class

#Here while calling the static output always we have to give an argument called (laptop),To avoid this we can use decrator.
#i.e above the class fuction  use @staticmethod 
