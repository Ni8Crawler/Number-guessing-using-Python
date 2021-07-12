#Imports the random module.
import random

random_list = ["1", "2", "3", "4", "5"]
initial_try = 0
max_tries = 3
out_of_try = False
num = ""

#Taking a random number from the list
random_num = random.choice(random_list)

while num != random_num and not(out_of_try):
    if initial_try < max_tries:
        num = input("Enter a number: ")
        initial_try += 1
    else:
        out_of_try = True

if out_of_try:
    print("Out of guesses, You lost")
else:
    print("Congratulations, You won!")