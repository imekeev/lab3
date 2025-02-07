from random import randint
name = input("Hello! What is your name?")
print(f"Well, {name}, I am thinking of a number between 1 and 20.")

x = randint(1, 20)

while True:
    n = int(input("Take a guess."))
    if n < x:
        print("Your guess is too low.")
    elif n > x:
        print("Your guess is too high.")
    else:
        print(f"Good job, {name}! You guessed my number in 3 guesses!")
        break
