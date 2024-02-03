# # # The for loop is usally used when the number of iteration is known.
# # # when we know the range for loop is used

# # # COunt the number of odd and even numbers betwwen 1 to 10 and print it
# # """
# # for i in range(1,13):
# #     if(i%2==0):
# #         print(i)
# # OUT PUT =
# # 2
# # 4
# # 6
# # 8
# # 10
# # 12

# # OUTPUT = 2
# # """

# # # count the number of odd and even numbers between 1 to 10 and print it.
# # """
# # e_count=0
# # o_count=0
# # for i in range(1,11):
# #     if(i%2==0):
# #         e_count=e_count+1
# #     else:
# #         o_count=o_count+1
# # print(e_count)
# # print(o_count)

# # OUTPUT +
# # 5
# # 5
# # """

# # # Count the number whch are are divisible by 3 and 5 , Range 1-100.
# # """
# # -----------------------------------------------------------------
# # for i in range(1,101):
# #     if(i%3==0 and i%5==0):
# #         print(i)
# # OUTPUT :
# # 15
# # 30
# # 45
# # 60
# # 75
# # 90
# # ----------------------------------------------
# # count=0
# # for i in range(1,101):
# #     if(i%3==0 and i%5==0):
# #         count=count+1
# # print(count)

# # OUTPUT : 6
# # ----------------------------------------------------------------------
# # """

# # """
# #  another way of SYNATX

# # result = [num for num in range(1, 101) if num % 3 == 0 and num % 5 == 0]
# # print(result)

# # OUTPUT : [15, 30, 45, 60, 75, 90]

# # count=len([num for num in range(1, 101) if num % 3 == 0 and num % 5 == 0])
# # print(count)


# # OUTPUT : 6

# # -----------------------------------------------------------------------
# # """

# # # Loops with List "[]"

# # # write a program to compute the sum of the first 5 natural number
# # """
# # sum=0
# # for i in range(1,6):
# #     sum=sum+i
# # print(sum)

# # OUTPUT : 15
# # -----------------------------------------------
# # """
# # #FOR LOOP
# # #Write a program to read 10 numbers fom the keyboard and find their sum and average.

# # '''
# # --------------------------------------------------------------
# # a=[]
# # for i in range(5):
# #     Keyboard=int(input("Enter the number "+str(i+1)+" :"))
# #     a.append(Keyboard)
# # print(a)

# # sum=0
# # for i in a:
# #     sum=sum+i
# # print(sum)

# # OUTPUT :
    
# # Enter the number 1 :1
# # Enter the number 2 :2
# # Enter the number 3 :25
# # Enter the number 4 :64
# # Enter the number 5 :56
# # [1, 2, 25, 64, 56]
# # 148    

# # -------------------------------------------------------------------

# # '''
# # # NESTED FOR LOOP
# # #print
# # #*
# # #**
# # #***
# # #****
# # """
# # for i in range(1,5):
# #     print()
# #     for j in range(1,i+1):
# #         print(j,end="")
# # OUTPUT:
  
# # 1
# # 12
# # 123
# # 1234  
# # """

# # """

# # for i in range(5):
# #     print()
# #     for j in range (1,i+1):
# #         print("*",end="")

# # OUTPUT :
# # *
# # **
# # ***
# # ****
# # ----------------------------------------------------------------

# # """
# # #WHILE LOOP - The while loop is usally used when the number of iteration is UNKNOW.
# # # When we dont know the range to give while loop is used

# # '''
# # i=0
# # while(i==0):
# #     print(i)
# #     i=i+1

# # OUTPUT : 0
# # '''

# # #while loop ended because after print we can given i=i+1 so that out will be 1,so it is not equul to 0 so while ended.
# # #if we have not i=i=1 the while loop of i==0 den it will keep on looping the input.

# # """
# # ------------------------------------------------------------------------------------
# # #1 Print a number from 1to5 using while loop

# # i=1
# # while(i<6):
# #     print(i)
# #     i=i+1
# # OUTPUT : 
# # 1
# # 2
# # 3
# # 4
# # 5
# # -------------------------------------------------------------------------------------------------
# # """
# # #2 write a loop statement to print the folling series 10,20,30,40,50,60,,,,,,,,200.
# # """
# # i=10
# # while(i<=200):
# #     print(i,end=",","")
# #     i=i+10

# # OUTPUT : 10,20,30,40,50,60,70,80,90,100,110,120,130,140,150,160,170,180,190,200,
# # ----------------------------------------------------------------------------
# # """

# # #3 Write a program to print first 10 natural number in reverse order.

# # """
# # i=10
# # while(i>0):
# #     print(i,end=",")
# #     i=i-1

# # OUTPUT  :10,9,8,7,6,5,4,3,2,1,

# # --------------------------------------------------------------------------
# # """

# #4 Write a program to find the factorial of a number
# # Factorial means multipling in the reversee order ( ! )


i=3
fact=1
while (i>0):
    fact=fact*i
    i=i-1
print(fact)

# OUTPUT : 6


RANDOM INPUT GAME 

import random

num = random.randint(1, 10)

guess = int(input("Can you guess the number I am thinking? It's less than 10 - "))
attempts = 3

while num != guess:
    if guess > num:
        print("Your guess is higher")
    else:
        print("Your guess is lower")
          

    attempts -= 1
    print("You have", attempts, "attempts to guess")

    if attempts == 0:
        print("You lost the game") 
        print ("You cant guess me. better lunck next time ")
        break

    guess = int(input("Guess again: "))

print ("Won ")
