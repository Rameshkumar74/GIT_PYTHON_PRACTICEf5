 Classes and Objects =>

1. Ramesh and suresh wants to go goa but both of them have different needs ramesh wants to "lets party" and suresh wants to "enjoy the beach"
HERE
 Goa is class
 Ramesh & Suresh are two objects
 Party and Beach is function (NOTE : SELFKEYWORD IS GIVEN AS PARAMETER/ARGUMENT BECAUSE WITHOUT PARAMETER FUUNTION WILL NOT WORK)

 
class goa:
    def party(self):
        print("Lets Party....")
    def beach(self):
        print("Enjoying the beach")

ramesh=goa()
suresh=goa()
 
 If we execute this object will enter into class :

Additionally let�s change the change and objects into capital letters .
HERE name is a variable
 class goa:
    name=""
    def party(self):
        print("Lets Party....")
    def beach(self):
        print("Enjoying the beach")

ramesh=goa()
suresh=goa()

ramesh.name="RAMESH"
suresh.name="SURESH"

print(ramesh.name)
print(suresh.name)

OUTPUT :
       RAMESH
       SURESH
 

additional executing one more variable "drink", execute the variables if ramesh drinks print "YES". and for suresh print "NO"
 
class goa:
    name=""
    drink=""
    def party(self):
        print("Lets Party....")
    def beach(self):
        print("Enjoying the beach")

ramesh=goa()
suresh=goa()

ramesh.name="RAMESH"
suresh.name="SURESH"

print(ramesh.name)
print(suresh.name)

ramesh.drink="YES"
suresh.drink="NO"

print("IS RAMESH WILL DRINK ? : ",ramesh.drink)
print("IS SURESH WILL DRINK ? : ",suresh.drink)

OUTPUT :
    RAMESH
    SURESH
    IS RAMESH WILL DRINK ? :  YES
    IS SURESH WILL DRINK ? :  NO   

 

NOW  EXECUTE THE ACTUALL QUESTION BY CALLING THE FUNCTION 
 
class goa:
    name=""
    drink=""
    def party(SELF):
        print("Lets Party....")
    def beach(self):
        print("Enjoying the beach")

ramesh=goa()
suresh=goa()

ramesh.name="RAMESH"
suresh.name="SURESH"

print(ramesh.name)
print(suresh.name)

ramesh.drink="YES"
suresh.drink="NO"

print("IS RAMESH WILL DRINK ? : ",ramesh.drink)
print("IS SURESH WILL DRINK ? : ",suresh.drink)

ramesh.party()
suresh.beach()


OUTPUT :
    RAMESH
    SURESH
    IS RAMESH WILL DRINK ? :  YES
    IS SURESH WILL DRINK ? :  NO
    Lets Party....
    Enjoying the beach

*************************************************************************
 

 2. Create a class called laptop and create a following variable and function.
    Variable => Price, Processor, Ram
    Create Object HP, Dell, Lenovo.
   50000,i5,16GB & 70000,i7,8GB & 80000,i9,16GB
   Print price of HP, Processor of Dell, Ram of Leneva.

 SOL :
 
class laptop:
    Price=0
    Processor=""
    Ram=""

HP=laptop()
Dell=laptop()
Lenova=laptop()

HP.Price=50000
HP.Processor="i5"
HP.Ram="16GB"

Dell.Price=70000
Dell.Processor="i7"
Dell.Ram="8GB"

Lenova.Price=80000
Lenova.Processor="i9"
Lenova.Ram="16GB"

print(HP.Price)
print(Dell.Processor)
print(Lenova.Ram)

OUTPUT :
    50000
    i7
    16GB

*************************************************************************

CONSTRUCTOR AND SELF KEYWORD

 
class laptop:
    def __init__(self):
        print("Demo")
    def display(self):
        print("Display")

hp=laptop()
 
Here we have created only the object,  we have not called the class to execute, even if we execute the output will be Demo.
Because the __init__ is executed here, this is inbuilt function called as constructor.
A constructor is a unique function that gets called automatically when an object is created of a class.
The main purpose of a constructor is to initialize or assign values to the data members of the class. 

USES:
When we create a class and object it will store in the memory of our PC, this constructor will define how much space is required for class and objects.

SELFKEYWORD = IS USED TO DENOTE THE CURRENT OBJECT.
 
class laptop:
    def __init__(self):
        self.ram=""
        self.processor="" 
    def display(self):
        print("Ram : ", self.ram)
        print("Processor : ",self.processor)
hp=laptop()

hp.ram="8gb"
hp.processor="i5"

hp.display()

If we Execute this the output will be (Price :  8gb Processor :  i5).
 
Expalination :
 
Here there is a laptop as class inside that there is an init(constructor) inside there is self.ram & self.processor and there is display function.
The display will print the self.ram and self.processor.
Now there is object called hp, whenever the object created the construct will call automatically to perform.
Then when we give hp.ram="8gb" it will store in the created constructor, then inside the Display we have given self.ram & self.processor.
When we give the self in .ram &.processor it will denote to the current object. the current object that we have is hp, now when we call hp.display(). The program will read as  hp.display(hp), this will call def display(self) inside this when we give print "Ram : ", self.ram. the Ram will print as it is and in the place of self it will denote to the hp.ram.

**********************************************************
 

1. Create a class called student
   Create a variable = name and register number using constructor.
   Create a function called display which should display the name and register number of the student.

 SOL
 

class student:
    def __init__(self):
        self.name="RAMESH"
        self.regno="625266"
    def display(self):
        print("Name : ",self.name)
        print("RegNO : ",self.regno)

s1=student()
s2=student()

s1.name="Manoj"
s1.regno="1"

s2.name="Karthi"
s2.regno="2"

s1.display()
s2.display()

OUTPUT : Name :  Manoj
         RegNO :  1
         Name :  Karthi
         RegNO :  2
*****************************************************************
 

3. Create a class called Fruit
   Create a variable called colour using__init__method
   Create an object called apple "Pass the colour variable as a parameter through object".

 SOL
 
class Fruit:
    def __init__(self,col):
        self.colour=col

apple=Fruit("Red")
print(apple.colour)        

OUTPUT : Red
********************************************************************
 

4. Create a class called teacher
   Create a variable = name and register number using constructor
   Create a function called display which should display the name and register number of the teacher
   Create t1 and t2 object and pass the name and reg no value through object

 SOL
 
class teacher:
    def __init__(self,name,reg):
        self.name=name
        self.regno=reg
    def display(self):
        print("Name",self.name)
        print("Reg NO",self.regno)
t1=teacher("Thomas","1")
t2=teacher("John","2")

t1.display()
t2.display()

OUTPUT : Name Thomas
         Reg NO 1
         Name John
         Reg NO 2
*******************************************************************************
 
4. Create a class called calculator
   Create 2 variables a and b
   Create a function  called add,sub,mul,div all functions should take 2 variables as parameter.
   Pass the a and b value through object().

SOL
 
ADD
class calculator:
    def __init__(self,a,b):
        self.num1=a
        self.num2=b
    def add(self):
        print("add ",self.num1+self.num2)

obj1=calculator(10,20)
obj1.add()

SUB
class calculator:
    def __init__(self,a,b):
        self.num1=a
        self.num2=b
    def sub(self):
        print("sub ",self.num1-self.num2)

obj1=calculator(20,10)
obj1.sub()

MUL
class calculator:
    def __init__(self,a,b):
        self.num1=a
        self.num2=b
    def mul(self):
        print("mul ",self.num1*self.num2)

obj1=calculator(20,10)
obj1.mul()

DIV

class calculator:
    def __init__(self,a,b):
        self.num1=a
        self.num2=b
    def div(self):
        print("div ",self.num1/self.num2)

obj1=calculator(20,10)
obj1.div()

OUTPUT : add  30
         sub  10
         mul  200
         div  2.0
*************************************************************************

