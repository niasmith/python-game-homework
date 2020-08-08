
print("Hello, welcome to my game!")
value = raw_input("What is your name?")
print("Let us play a game!")
print("This is a number guessing games")

import random

hidden = random.randrange(1, 201)
print(hidden)

guess = int(input("Please guess a number"))

if guess == hidden:
    print("Correct answer!")
elif guess < hidden:
    print("You're too low")
else:
    print("You're too high")

# while loop
# index = 0
# while True:
#     print(index)
#     index += 0
#     if index < 10:
#         break;