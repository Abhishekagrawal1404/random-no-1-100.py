import random

def play_game():
    secret_number = random.randint(1, 100)
    attempts = 0
    print("I'm thinking of a number between 1 and 100. Can you guess it?")
    while True:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1
            if guess == secret_number:
                print("Congratulations! You guessed the number in", attempts, "attempts.")
                break
            elif guess < secret_number:
                print("Too low, try again.")
            else:
                print("Too high, try again.")
        except ValueError:
            print("Invalid input. Please enter an integer between 1 and 100.")

play_game()
