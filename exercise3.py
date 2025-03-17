#Author:Wulei
#DATE:2025/3/14
#import the random from outside
import random

random_number = random.randint(10, 20)

while True:
    try:
        b = int(input("Enter the number you guess: "))
        
        if b > random_number:
            print("Too big")
        elif b < random_number:
            print("Too small")
        elif b == random_number:
            print("Congratulations")
            break
        else:
            print("Please enter the correct number")
    except ValueError:
        print("Invalid input! Please enter a number.")
