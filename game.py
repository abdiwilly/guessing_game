# this program demonstrates a guessing game
#get user input
#generate random number
#using a while loop
#check if user input is equal o generated number
from random import randint

username=input("Enter your name:")
print("Hello"+ " " + username)

random_number=randint(10,50)

counter=0
while counter <5:
    user_number=eval(input("Enter a number:"))
    counter += 1
    if  user_number < random_number:
        print("your guess is low")
    elif user_number > random_number:
        print("Your guess is too high")
    elif "user_name" == random_number:
        print("you win but you are still a looser")
        break


if user_number == random_number:
    print("You win")
else:
    print("game over the correct number is:")
    print(random_number)
