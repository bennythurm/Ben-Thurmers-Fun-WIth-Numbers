"""Fun With Numbers By Ben Thurmer"""
#Ben Thurmer
# credit to nick dingle for the original fun with numbers
import os
import time
import random
NUMBER_COUNT = 0
NUMBER_TOTAL = 0
SMALLEST_NUMBER = 0
LARGEST_NUMBER = 0
PLOT_COUNT = 0

def main():
    """what the user first sees on the landing page"""
    intro_screen()
    load()
    exit_flag = False
    while not exit_flag:
        clear()
        print("Welcome To Fun With Numbers!")
        print("\n Choose From The Menu Below")
        print(" (A) Check number features")
        print(" (B) Plot numbers")
        print(" (C) Check overall stats")
        print(" (D) Guess a number game")
        print(" (E) Calculator")
        print("\n (X)  Save and exit")
        choice = input("\n Choice:") .upper()

        if choice == "A":
            numberfeatures()
        elif choice == "B":
            plotter()
        elif choice == "C":
            stats()
        elif choice =="D":
            number_guessing_game()
        elif choice == "E":
            calculator()
        elif choice == "X":
            saves()
            exit_flag = True
        else:
            print("Invalid Response Try Again Please")

def numberfeatures():
    """shows the user what features the number has"""
    clear()
    number = int(input("Please enter a WHOLE number to be checked over: "))
    clear()
    global NUMBER_COUNT , NUMBER_TOTAL , SMALLEST_NUMBER , LARGEST_NUMBER
    print(f" The features of {number} are...")

        #Determines if number is positive or negative
    if  number > 0:
        print("\n Your Number Is Positive")
    elif number < 0:
        print("\n Your Number Is Negative")
    else:
        print("\n Your Number Is Zero")

    #Determines if number is even or odd
    if number % 2 == 0:
        print(" Your Number Is Even")
    else:
        print(" Your Number Is Odd")

    #Lists the factors of the number
    factor_count = 0
    print(" The number factors are...", end="")
    for i in range(1, number + 1):
        if number % i == 0:
            print(" " + str(i), end="")
            factor_count += 1

    #Indicates if number is prime or not
    if factor_count == 2:
        print("\n Your Number Is a prime number")
    else:
        print("\n Your Number Is not a prime number")

    input("\n Press Enter to continue...")

    #updates global variables
    if NUMBER_COUNT == 0:
        SMALLEST_NUMBER = number
        LARGEST_NUMBER = number
    else:
        SMALLEST_NUMBER = min(number, SMALLEST_NUMBER)
        LARGEST_NUMBER = max(number, LARGEST_NUMBER)

    NUMBER_COUNT += 1
    NUMBER_TOTAL += number

def plotter():
    """able to plot a number on a map"""
    clear()
    global PLOT_COUNT
    num_columns = 38
    num_rows = 12
    table = [[" " for column in range(num_columns)]for row in range (num_rows)]

    while True:
        try:
            #prompt user for x  y axis to plot on the map
            clear()
            x_axis = int(input("Please enter a x axis to plot on the map ( 1 - 38): "))
            y_axis = int(input("Please enter a y axis to plot on the map ( 1 - 12): "))

            #makes sure values that are entered are integers and are valid
            input("\n press enter to continue")
            if 1 <= x_axis <= 38 and 1 <= y_axis <= 12:
                table[y_axis - 1][x_axis - 1] = "X"
                #updates the plot count for each time it is used
                PLOT_COUNT += 1
                print_table(table)
            #prompts user if they want to plot another co ordinatie
            anotherplot = input("Do you want to plot another co ordinatie? (y/n): ").lower()
            if anotherplot != "y":
                break
            else:
                print("\n Invalid Input Please use valid coordinates")
        except ValueError:
            print("\n Invalid Input Please use intergers coordinates")

def print_table(table):
    """prints a table"""
    print("\n                                                       x axis")
    print("    1  2  3  4  5  6  7  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 ")
    print("    --------------------------------------------------------------------------------------------------------------")
    for index, row in enumerate(table, start = 1):
        print(f"{index:2} | {'  '.join(row)} |")
    print("    --------------------------------------------------------------------------------------------------------------")

def stats():
    """shows your stats used overall on the app"""
    clear()
    print("Here is your stats used overall on the app:")
    print(f"\n Numbers Entered:{NUMBER_COUNT}")
    print(f" Total of numbers: {NUMBER_TOTAL}")
    if NUMBER_COUNT != 0:
        print(f" Average of numbers: {NUMBER_TOTAL/NUMBER_COUNT}")
    else:
        print(f" Average of numbers: {NUMBER_TOTAL-NUMBER_COUNT}")
    print(f" Smallest number entered: {SMALLEST_NUMBER}")
    print(f" Largest number entered: {LARGEST_NUMBER}")
    print(f" Coordinated Plotted: {PLOT_COUNT}")
    input("\n Press Enter to continue...")

def number_guessing_game():
    """A simple number guessing game."""
    # Generate a random number between 1 and 100
    clear()
    secret_number = random.randint(1, 100)
    attempts = 0
    #landing screen
    print("Welcome to the Number Guessing Game!")
    print("I have chosen a number between 1 and 100. Can you guess it?")

    while True:
        guess = int(input("Enter your guess (between 1 and 100): "))
        attempts += 1

        if guess < secret_number:
            print("Too low! Try again.")
        elif guess > secret_number:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You guessed the number {secret_number} in {attempts} attempts!")
            input("Press Enter To Continue")
            break

def calculator():
    """basic calculator program"""
    clear()
    operation = input("""
    Please enter the operation you wish to use                
    + for addition
    - for subtractiom
    * for multiplication
    / for division              
    """)

    number_1 = int(input("Enter Your First Number "))
    number_2 = int(input("Enter Your Second Number "))

    #addition
    if operation == "+":
        print("{} + {}".format(number_1, number_2))
        print(number_1 + number_2)

    #subtraction
    elif operation == "-":
        print("{} + {}".format(number_1, number_2))
        print(number_1 - number_2)

    #Multiplication
    elif operation == "*":
        print("{} + {}".format(number_1, number_2))
        print(number_1 * number_2)

    #division
    elif operation == "/":
        print("{} + {}".format(number_1, number_2))
        print(number_1 / number_2)

    else:
        print("you have not entered a valid operation")

    #asks the user if they want to cal ulate another number
    calc_again = input("""
    Do you want to calculate another number?
    Please Type Y For Yes or N For No
    """).strip().lower()

    if calc_again == "y":
        calculator()

def intro_screen():
    """intro screen that shows a bit of info aboout ther program"""
    intro_text = ("""
    Welcome To Fun With Numbers!
    This program offers various number-related functionalities.
    Let's explore numbers together!
                  
    """)
    clear()
    # Display scrolling intro text
    for char in intro_text:
        print(char, end='', flush=True)
        time.sleep(0.012)  #how fast the text moves
    input("\n    Press Enter to continue...")

# Other functions and main remain the same...

def clear():
    """clears the screen"""
    os.system('cls' if os.name == 'nt' else 'clear')

def saves():
    """saves the users numbers"""
    with open("stats.txt", "w" , encoding="utf-8") as file:
        file.write(f"{NUMBER_COUNT}\n")
        file.write(f"{NUMBER_TOTAL}\n")
        file.write(f"{SMALLEST_NUMBER}\n")
        file.write(f"{LARGEST_NUMBER}\n")
        file.write(f"{PLOT_COUNT}\n")

def load():
    """loads the users numbers"""
    if not os.path.exists("stats.txt"):
        return

    with open("stats.txt", "r", encoding="utf-8") as file:
        global NUMBER_COUNT , NUMBER_TOTAL , SMALLEST_NUMBER , LARGEST_NUMBER , PLOT_COUNT
        NUMBER_COUNT = int(file.readline())
        NUMBER_TOTAL = int(file.readline())
        SMALLEST_NUMBER = int(file.readline())
        LARGEST_NUMBER = int(file.readline())
        PLOT_COUNT = int(file.readline())
main()
