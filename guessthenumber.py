import random
no = random.randint(1,10)

player_name = input("Hello, Welcome, What's your name? ")
no_guesses = 0
print('okay good!Hello '+player_name+' I will be guessing a number which falls in between 1 to 10......can you guess the number? ')

while no_guesses <3:
    guess = int(input())
    no_guesses+=1
    if guess<no:
        print("Your guess it too low ")
    elif guess>no:
        print('Your guess is too high ')
    else:
        break

if guess == no:
    print("You guessed the number in "+str(no_guesses)+' guesses')
else:
    print("You lost try again.  ")














































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































