import numpy as np
import time

def number_guessing_game():
    number = np.random.randint(1, 101)

    print("\nWelcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    print("\nSelect your difficulty level:")
    print("1. Easy (10 chances)")
    print("2. Medium (5 chances)")
    print("3. Hard (3 chances)")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        print("You selected Easy difficulty.")
        chances = 10
    elif choice == 2:
        print("You selected Medium difficulty.")
        chances = 5
    elif choice == 3:
        print("You selected Hard difficulty.")
        chances = 3
    else:
        print("Invalid choice!")
        return

    print("\nLet's start the game!")

    start_time = time.time()
    won = False

    for i in range(chances):
        guess = int(input("\nEnter your guess: "))

        if guess == number:
            print(f"\nCongratulations! You guessed the number in {i+1} attempts.")
            won = True
            break

        elif guess < number:
            print(f"Incorrect! The number is greater than {guess}.")

        else:
            print(f"Incorrect! The number is less than {guess}.")

    else:
        print("\nSorry! You've run out of chances.")
        print(f"The correct number was {number}.")

    end_time = time.time()
    time_taken = end_time - start_time

    print(f"\nTime taken: {time_taken:.2f} seconds")


def main():
    play_again = "yes"

    while play_again == "yes":
        number_guessing_game()
        play_again = input("\nDo you want to play again? (yes/no): ").lower()

    print("\nThanks for playing!")


main()
