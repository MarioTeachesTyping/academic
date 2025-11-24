##########################################
## ************************************ ##
## * Written By..: Anthony Terry (AJ) * ##
## * Date Written: November 1, 2023   * ##
## * Purpose.....: Temperature Menu   * ##
## ************************************ ##
##########################################

import random
import statistics

def main():

    choice = '100'
    # This will hold random or inputted temperatures from the user.
    tempList = []
    while(choice != '5'):
        choice = getChoiceFromUserAfterIDisplayTheMenu()
        # Get 1 temperature from the user.
        if(choice == '1'):
            getOneTemperatureFromUser(tempList)
        # Generate 10 random temperatures for the user.
        elif(choice == '2'):
            getTenRandomTemperatures(tempList)
        # Display all temperatures from hot to cold.
        elif(choice == '3'):
            displayAllTemperaturesOrderedFromHighToLow(tempList)
        # Display stats for temperatures.
        elif(choice == '4'):
            displayTemperatureStats(tempList)
        # Quit Program.
        elif(choice == '5'):
            print()
            marquee("Have a Great Day. Eat SNICKERS!")
            pause()
        else:
            print()
            marquee("Invalid Menu Selection. Try Again.")
            pause()

#---------------------------------------------------------------------------------------------------

def calcFahrenheitToCelsius(value):

    # This will turn degrees of Fahrenheit into degrees of Celsius.
    result = (value - 32) * 5 / 9

    # Format the result to only display one decimal point to match with Fahrenheit.
    result = '{:.1f}'.format(result)
    return result

#---------------------------------------------------------------------------------------------------

def cls():

    # Creates an empty space to make our code look nice.
    print("\n" * 100)

#---------------------------------------------------------------------------------------------------

def displayAllTemperaturesOrderedFromHighToLow(tempList):

    # If no temperatures are in our list, the program will tell the user this information.
    if(len(tempList) == 0):
        print()
        marquee("There are no Temperatures to show. Try Selection 1 or 2 in the Main Menu.")
        pause()
        return
    print()
    marquee("List of Temperatures")
    print()

    # This will sort the list in descending order (high to low).
    sortedTempList = sorted(tempList, reverse = True)

    # This creates a list of all temperatures stored in our list starting from 1. \t means tab.
    for i in range(len(tempList)):
        print(str(i + 1) + '.\t', sortedTempList[i], "F\t \t-\t", calcFahrenheitToCelsius(sortedTempList[i]), "C")
    pause()

#---------------------------------------------------------------------------------------------------

def displayTemperatureStats(tempList):

    # If no temperatures are in our list, the program will tell the user this information.
    if(len(tempList) == 0):
        print()
        marquee("There are no Temperatures to show. Try Selection 1 or 2 in the Main Menu.")
        pause()
        return

    # Variables needed to get highest, lowest, average, and median temperature in Fahrenheit and Celsius.
    highestTemperatureF = max(tempList)
    lowestTemperatureF = min(tempList)
    averageTemperatureF = sum(tempList) / len(tempList)
    medianTemperatureF = statistics.median(tempList)
    highestTemperatureC = calcFahrenheitToCelsius(highestTemperatureF)
    lowestTemperatureC = calcFahrenheitToCelsius(lowestTemperatureF)
    averageTemperatureC = calcFahrenheitToCelsius(averageTemperatureF)
    medianTemperatureC = calcFahrenheitToCelsius(medianTemperatureF)

    # This will display the highest, lowest, average, and median temperatures in Fahrenheit and Celsius.
    print()
    marquee("Temperature Statistics")
    print()
    print(f"Highest Temperature: ", f"{highestTemperatureF:.1f}", "F\t \t-\t", highestTemperatureC, "C")
    print(f"Lowest Temperature.: ", f"{lowestTemperatureF:.1f}", "F\t \t-\t", lowestTemperatureC, "C")
    print(f"Average Temperature: ", f"{averageTemperatureF:.1f}", "F\t \t-\t", averageTemperatureC, "C")
    print(f"Median Temperature.: ", f"{medianTemperatureF:.1f}", "F\t \t-\t", medianTemperatureC, "C")
    pause()

#---------------------------------------------------------------------------------------------------

def getChoiceFromUserAfterIDisplayTheMenu():

    # This is the menu our user will see during the program.
    result = ''
    cls()
    marquee("   M A I N   M E N U   ")
    menu = "\n1. Get a Temperature from the User"
    menu += "\n2. Generate 10 Random Temperatures"
    menu += "\n3. Display All Temperatures Ordered High to Low"
    menu += "\n4. Display Temperature Stats"
    menu += "\n5. Quit"
    menu += "\n"
    menu += "\nEnter Your Selection: "
    result = input(menu)

    return result

#---------------------------------------------------------------------------------------------------

def getFloat(string):

    # This variable assumes the users input is invalid unless proven otherwise.
    badValue = True

    # The while loop ensures the user enters a floating point number.
    # If the user does not enter a number, the loop will restart.
    while(badValue):
        try:
            value = float(input(string))
            badValue = False
        except:
            badValue = True
            print()
            marquee("You Must Enter a Valid Number.")
            pause()
    return value

#---------------------------------------------------------------------------------------------------

def getOneTemperatureFromUser(tempList):

    # Variables needed for lowest and highest number of degrees in Fahrenheit.
    low = -200
    high = 500
    value = 5555

    # Asks user for temperature and checks if number inputted from user is between low and high boundaries.
    while(value < low or value > high):
        value = getFloat("\nEnter a Temperature in Fahrenheit: ")
        # If temperature inputted is below low or above high boundary the user cannot proceed.
        if(value < low or value > high):
            print()
            mess = "You Must Enter a Temperature in the Range of " + str(low) + " and " + str(high) + "."
            marquee(mess)
            pause()
    # The temperature added by the user is put into our list.
    tempList.append(value)
    print()
    marquee("1 Temperature has been Added to the List of Temperatures.")
    pause()

#---------------------------------------------------------------------------------------------------

def getTenRandomTemperatures(tempList):

    # Variables needed for lowest and highest number of degrees in Fahrenheit.
    low = -200
    high = 500

    # This will add 10 random number temperatures into our list.
    for i in range(10):
        tempList.append(random.randint(low, high))
    print()
    marquee("10 Temperatures in Fahrenheit Have Been Stored.")
    pause()

#---------------------------------------------------------------------------------------------------

def marquee(mess):

    # This function creates a unique border for whatever message we desire.
    symbol = '='
    size = len(mess) + 6
    print(symbol * size)
    print(symbol * 2, mess, symbol * 2)
    print(symbol * size)

#---------------------------------------------------------------------------------------------------

def pause():

    # This stops the program until the user presses Enter on their keyboard.
    input("\nPress ENTER to Continue...")

main()