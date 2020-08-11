
print('Hello, welcome to my game!')
name = raw_input('What is your name?' + ":")
print(str(name) +  ',Let us play a game!')

import random

flag = True
while flag:
    num = input('Type a number for an upper bound: ')
    if str(num).isdigit():
        print("Let's go y'all!")
        num = int(num)
        flag = False
    else:
        print('Please type a valid number')

secret = random.randint(1,num)

guess = None
count = 1

while guess != secret:
    guess = input('Please type a number between 1 and ' + str(num) +":  ")
    if str(guess).isdigit() :
        guess = int(guess)

        if guess < secret:
            print('Too low, guess again!')  
        if guess > secret:
            print('Too high, try again!')   
         
        if guess == secret:
            print('Correct')               
            count += 1

print('It took you', str(count), 'guesses!')            
