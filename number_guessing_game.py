import random

"""
In this program we will create a game where the user will guess a number between 1-200,
generated randomly and until they get the number the program will keep running and
keep the number of attempts it took for them to guess that number. """

def number_guessing ():
    # number: generate a random integer between 1-200
    number = random.randint(1, 200)
    #attempt: will hold the number of attempts it took to guess number
    attempts = 0

    print("WELCOME TO THE NUMBER GUESSING GAME!!")
    print("I am thinking of a number between 1-200. Can you guess it?")

    while True:
        try:
            guess = int(input("Enter a number: "))
            attempts += 1

            if guess < number:
                print("too low.")
            elif guess > number:
                print("TOO HIGH.")
            else:
                print(f"CONGRAGULATIONS!! You guessed the correct number in {attempts} attempts.")
                break
        except ValueError:
            print("Invalid Input. Please enter a integer.")

if __name__ == "__main__":
    number_guessing()

        
