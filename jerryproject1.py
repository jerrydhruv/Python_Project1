""" First Mini Project.
Guess the Number.(Guessing GAME)"""

import random

target = random.randint(1, 100)

while True:
    userChoice = int(input("Guess the target : "))
    if(userChoice == target):
        print("Success : Correct Guess !!")
        break
    elif(userChoice < target):
        print("your number was too small. Take a bigger guess..")
    else:
        print("your number was too big. Take a smaller guess..")


print("-----GAME OVER-----")    

# import random

# target = random.randint(1, 100)

while True:
    userChoice = input ("Guess the targt or Quit(Q) : ")
    if(userChoice == "Quit"):
        break
    
    userChoice = int(userChoice)
    if(userChoice == target):
        print("Success : Correct Guess!!")
        break
    elif(userChoice < target):
        print("your number was too small. Take a biger guess..")
    else:
        print("your number was too big. take a smaller guess..")


print("-----GAME OVER-----")

# """ Project2. Random Password Generator."""
 
import random
import string

pass_len = 6
charValues = string.ascii_letters + string.digits + string.punctuation

"""List comprehension [function for i in range(n)]"""

res = "%".join([random.choice(charValues) for i in range(pass_len)])
print(res)

"""Loop method of password generator."""
# password = ""
for i in range(pass_len):
    password += random.choice(charValues)

print("your random password is:", password)

