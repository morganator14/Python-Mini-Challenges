import random

def number_guess_game(level, random_number):
    if level == "easy":
        guesses = 10
    else:
        guesses = 5
    guess = guesses
    while guess > 0:
        user_guess = int(input("Your guess: "))
        if user_guess == random_number:
            print("Thats the number, you win!")
            guess = 0
            return
        elif user_guess > random_number:
            print("Too high")
            guess -= 1
            print(f"You have {guess} guesses left.")
        else:
            print("Too low")
            guess -= 1
            print(f"You have {guess} guesses left.")
    else:
        print(f"You are out of guesses, the number was {random_number}.")

def run_game():
    print("Welcome to the number guesser.")
    level = input("Would you like to play they easy or hard level?")
    random_number = random.randint(1,100)
    if level == "easy":
        number_guess_game("easy", random_number)
    else:
        number_guess_game("hard", random_number)

    restart = input("Would you like to play again?")
    if restart == "yes":
        print("n/" * 20)
        run_game()
    else:
        print("See you later")

run_game()
