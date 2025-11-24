##################################################################
## ************************************************************ ##
## * Written By: Anthony Terry, Adrian Badillo, Kimberly Leon * ##
## * Date Written: October 11, 2023                           * ##
## * Purpose: inClassRacingChallenge                          * ##
## ************************************************************ ##
##################################################################

import random
import time

def main():

    # Our variables for race length, and 3 race cars.
    raceLength = 100
    carA = 0
    carB = 0
    carC = 0

    while (carA < raceLength and carB < raceLength and carC < raceLength):
        carA, carB, carC = moveCars(carA, carB, carC)
        displayCars(carA, carB, carC, raceLength, True)
    cls()
    displayCars(carA, carB, carC, raceLength, False)
    displayResults(carA, carB, carC)
    print(input("\nPress ENTER to Continue."))

# -----------------------------------------------------------------------------------
def moveCars(a, b, c):

    lb = 1
    ub = 3
    car = random.randint(lb, ub)
    spaces = random.randint(lb, ub)
    if (car == 1):
        a += spaces
    elif (car == 2):
        b += spaces
    else:
        c += spaces
    return a, b, c

# -----------------------------------------------------------------------------------
def displayCar(letter, x):

    for i in range(x):
        print(letter, end="")
    print()

# -----------------------------------------------------------------------------------
def displayCars(a, b, c, raceLength, nothing):

    cls()
    for i in range(raceLength):
        print(' ' * (raceLength - 6) + 'FINISH')
        print('.' * (raceLength - 1) + '|')
        displayCar('A', a)
        displayCar('B', b)
        displayCar('C', c)
        if (nothing):
            delay()
            cls()

# -----------------------------------------------------------------------------------
def displayResults(a, b, c):

    if (a > b and a > c):
        print("\n1st Place: A")
    if (b > a and b > c):
        print("\n1st Place: B")
    if (c > a and c > b):
        print("\n1st Place: C")
    if (a > b and a < c):
        print("2nd Place: A")
    if (a > c and a < b):
        print("2nd Place: A")
    if (b > a and b < c):
        print("2nd Place: B")
    if (b > c and b < a):
        print("2nd Place: B")
    if (c > a and c < b):
        print("2nd Place: C")
    if (c > b and c < a):
        print("2nd Place: C")
    if (a < b and a < c):
        print("3rd Place: A")
    if (b < a and b < c):
        print("3rd Place: B")
    if (c < a and c < b):
        print("3rd Place: C")

# -----------------------------------------------------------------------------------
def cls():

    print('\n' * 100)

# -----------------------------------------------------------------------------------
def delay():

    time.sleep(0.00001)

main()