#SnakeWaterGun Game Using Python

import random
import time
lst=["Snake","Water","Gun"]
#print(choice)
com=0
me=0
print("Welcome To SnakeWaterGun Game!")
#n=int(input("enter 1 for Snake, 2 for Water, 3 for Gun"))
print("Game is starting........")
time.sleep(3)
for i in range(1,11):
    print("                         Round-",i)
    print()
    n=input("enter any key given below\nS:Snake\nW:Water\nG:Gun:\n")
    print()
    choice=random.choice(lst)
    if(n=="S" or n=="s"):
        n="Snake"
    elif(n=="W" or n=="w"):
        n="Water"
    elif(n=="G" or n=="g"):
        n="Gun"

        
    if("Snake"==n and choice=="Water"):
        print("your choice is :"+n)
        print("computer's choice is :"+choice)
        print("you are winner!")
        me=me+1
    elif("Snake"==n and choice=="Gun"):
        print("your choice is :"+n)
        print("computer's choice is :"+choice)
        print("computer is winner!")
        com=com+1
    elif("Water"==n and choice=="Snake"):
        print("your choice is :"+n)
        print("computer's choice is :"+choice)
        print("computer is winner!")
        com=com+1
    elif("Water"==n and choice=="Gun"):
        print("your choice is :"+n)
        print("computer's choice is :"+choice)
        print("you are winner!")
        me=me+1
    elif("Gun"==n and choice=="Snake"):
        print("your choice is :"+n)
        print("computer's choice is :"+choice)
        print("you are winner!")
        me=me+1
    elif("Gun"==n and choice=="Water"):
        print("your choice is :"+n)
        print("computer's choice is :"+choice)
        print("computer is winner!")
        com=com+1
    elif("Gun"==n and choice=="Gun" or n=="Snake" and choice=="Snake" or n=="Water" and choice=="Water"):
        print("Both are same!")
    else:
        print("Invalid Entery!")
if(me>com):
    print()
    print("You win the match",me,"times")
elif(me==com):
    print()
    print("Match is draw!")
else:
    print()
    print("computer win the match",com,"times")



