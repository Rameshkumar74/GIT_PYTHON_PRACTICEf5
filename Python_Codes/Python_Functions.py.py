# Python Functions :
# TO Create a Function ' def ' should be used
# If we use def the program will skip this , assuming this is a function and it will move on another one
# later when we call that fuction name it will start impleting.

# QUESTIONS :

#1.Create a fution called add(), sub(), mul(), div()
#   And get the input for a and b inside every function then print the result.
"""
def add():
    a=int(input("Enter a number for addtion : "))
    b=int(input("Enter a number for addtion : "))
    print(("Total : "),(a+b))
    

# If we print it will not excute , Until we call the fuction name "add".
#How to call - Just type the function name and execute.

add()

OUTPUT : Enter a number for addtion : 20
          Enter a number for addtion : 30
          Total :  50

def sub():
    a=int(input("Enter a number for Subbraction : "))
    b=int(input("Enter a number for Subbraction : "))
    print(("Total : "),(a-b))
    
sub()

OUTPUT : Enter a number for Subbraction : 50
          Enter a number for Subbraction : 30
          Total :  20

******************************************************************************
"""
"""
def mul():
    a=int(input("Enter a number to Multiply : "))
    b=int(input("Enter a number to Multiply : "))
    print(("Total : "),(a*b))
    
mul()

OUTPUT : Enter a number to Multiply : 5
         Enter a number to Multiply : 2
         Total :  10
*************************************************************************
"""
"""
def div():
    a=int(input("Enter a number to Divide : "))
    b=int(input("Enter a number to Divide : "))
    print(("Total : "),(a/b))

div()

OUTPUT : Enter a number to Divide : 25
         Enter a number to Divide : 5
         Total :  5.0
***************************************************************************
"""

"""
def add():
    a=int(input("Enter a number for addtion : "))
    b=int(input("Enter a number for addtion : "))
    print(("Total : "),(a+b))

def sub():
    a=int(input("Enter a number for Subbraction : "))
    b=int(input("Enter a number for Subbraction : "))
    print(("Total : "),(a-b))

def mul():
    a=int(input("Enter a number to Multiply : "))
    b=int(input("Enter a number to Multiply : "))
    print(("Total : "),(a*b))
    
def div():
    a=int(input("Enter a number to Divide : "))
    b=int(input("Enter a number to Divide : "))
    print(("Total : "),(a/b))

#We can call enter function at a time

add()

sub()

mul()

div()

OUTCOME :
Enter a number for addtion : 50
Enter a number for addtion : 30
Total :  80
Enter a number for Subbraction : 50
Enter a number for Subbraction : 30
Total :  20
Enter a number to Multiply : 50
Enter a number to Multiply : 30
Total :  1500
Enter a number to Divide : 50
Enter a number to Divide : 30
Total :  1.6666666666666667
    
******************************************************************************
"""
"""
****
#Creating a function by variable/Parameter/Arguments :
#(msg) is the parameter

def painter(msg):
    print("Message : ",msg)

painter("Paint my house")

OUTPUT : Message :  Paint my house

*****************************************************************************
"""

# FUNCTION WITH IF ELSE :

#2. Get a integer number from user and pass it to the funtion called findevenorodd().
#   Let the function print wheather the number is even or odd.
"""
#SOL :

def findevenorodd(b):
    if(b%2==0):
        print("Even")
    else:
        print("Odd")
a=int(input("Enter a number find odd or Even = " ))    
findevenorodd(a)

OUTPUT : if we enter 20
Enter a number find odd or Even = 20
Even

OUTPUT : if we enter 21
Odd
*********************************************************************************
"""

#3. Get a integer number from user and pass it to the funtion called findpassorfall().
#   Let the function print whether the number is pass or fail.

"""
#SOL :

def findpassorfail(b):
    if(b<35):
        print("Fail")
    else:
        print("Pass")
a=int(input("Enter your Marks to know Pass or Fail = "))
findpassorfail(a)

OUTPUT : If we type 87
Enter your Marks to know Pass or Fail = 87
Pass

OUTPUT : If we type 34
Enter your Marks to know Pass or Fail = 34
Fail

**********************************************************************************************
"""

# FUNCTION WITH LOOPING :

#4. Get the input for a and b and pass it to the function called printrange().
#   Let the function print numbers from a to b.

"""
#SOl

def printrange(R1,R2):
    for i in range(R1,R2):
        print(i,end=",")
a=int(input("Enter a : "))
b=int(input("Enter B : "))
printrange(a,b)

OUTPUT :
Enter a : 21
Enter B : 51
21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,

******************************************************************************************
"""

#RETURN KEYWARD IN PYTHON FUNCTION =

#5. Set s_username="EMC" s_password="123"
#   Get input for username and password
#   Create a function called validate
#   if username and password matches the function should return True else False.
"""
# SOL :


s_username="EMC"
s_password="123"

username=input( "USER NAME TO LOGIN : ")
password=input("PLEASE ENTER YOUR PASSWORD : ")

def validate():
    if(s_username==username and s_password==password):
        return True
    else:
        return False

a=validate()
print(a)

OUTPUT :
USER NAME TO LOGIN : EMC
PLEASE ENTER YOUR PASSWORD : 123
True
    
********************************************************************************************
"""

#6.(a+b)*c
#   Get input for a and b and function called add() which should return the sum of a and b
#   And multiply that sum with c

"""s
# SOL :

def add(n1,n2):
    return n1+n2

a=int(input("a :"))
b=int(input("b :"))
c=int(input("c :"))

added=add(a,b)
output=added*c

print(output)

OUTPUT :
a :10
b :20
c :10
300

**********************************************************************************************
"""

#1 Keyword Arg
"""
def per (name ,age):
    print(name)
    print(age)
print(56,"ram")
per(age=56,name="ram")

#OUtPUT 56 ram

"""
"""
def per (name ,age):
    age=age+18
    print(age,name )

per(age=56,name="ram")

OUTPUT :74 ram


#IF we use the keyword arg in the start we have give the folling inthr keyword arg itself

per (age=16 name = ram,year =2016)

# Incase if we give the value, frurther we cn give keyword arg

per("ram", year = 2016, age=19)
*********************************************************************
"""

# default arg
"""
def per(name,age=18):
    print(name,age)
per("ram",28)

OUTPUT = 28
if we give age =28 it will overrist and print 28 
"""
#Varaiblr lenght arg
#print(l)

"""
def sum(a,b):
    c=a
    for i in b:
        c=c+1
print(c)

"""

#****************************************
"""
def add():
    a=int(input("Enter a number for addtion : "))
    b=int(input("Enter a number for addtion : "))
    print(("Total : "),(a+b))
    
def sub():
    a=int(input("Enter a number for Subbraction : "))
    b=int(input("Enter a number for Subbraction : "))
    print(("Total : "),(a-b))

add()
sub()

#Passig the integer number to the funtion called findpassorfall().
   
def findpassorfail(b):
    if(b<35):
        print("Fail")
    else:
        print("Pass")
a=int(input("Enter your Marks to know Pass or Fail = "))
findpassorfail(a)

*************************
"""
# passing the input into the function called printrange().

def printrange(R1,R2):
    for i in rane(R1,R2):
        print(i,end=",")
a=int(input("Enter a : "))
b=int(input("Enter B : "))
printrange(a,b)
