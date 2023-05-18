import random

#generate random number from 1 to 100
number = random.randint(1, 100)
print(number)

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
difficulty = (input("Choose a difficulty. Type 'easy' or 'hard': ").lower())

attempt = int(0)

def guesses():
    global attempt
    print(f"You have {attempt} attempts remaining to guess the number.")
    
    #end game or continue
    if attempt == 0:
        print("Game Over!")
    else:
        guess = int(input("Make a guess: "))

        #Compare number and guess
        if guess > number:
            print("Too high.")
            attempt -= 1
            guesses()
        elif guess < number:
            print("Too low.")
            attempt -= 1
            guesses()
        else:
            print(f"You got it. The answer is {guess}")

#Choode difficulty
if difficulty == ("easy"):
    attempt = int(5)
    guesses()
elif difficulty == ("hard"):
    attempt = int(10)
    guesses()
else:
    print("you entered an invalid response."))
