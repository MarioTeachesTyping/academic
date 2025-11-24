####################################################
## ********************************************** ##
## * Written By..: AJ, Adrian, Chris, Kim, Meli * ##
## * Date Written: November 8, 2023             * ##
## * Purpose.....: Exam Scores & Grade Book     * ##
## ********************************************** ##
####################################################

def main():

    choice = '100'
    # This will hold our exam scores for the grade book.
    gradesList = []
    while(choice != '7'):
        choice = getChoiceFromUserAfterDisplayMenu()
        # Asks the user for one exam score between 0 and 100.
        if(choice == '1'):
            getOneExamScore(gradesList)
        # Asks the user for exam scores between 0 and 100 until user enters -999.
        elif(choice == '2'):
            getExamScoresTillValue(gradesList)
        # Display exam scores from highest to lowest, and lowest to highest.
        elif(choice == '3'):
            displayAllExamScores(gradesList)
        # Display exam statistics like highest, lowest, average scores, and number of each letter grade.
        elif(choice == '4'):
            displayExamStats(gradesList)
        # Reduces all exam scores by 5 points.
        elif(choice == '5'):
            reducesAllExamScoresByFive(gradesList)
        # Removes all F grades from the list.
        elif(choice == '6'):
            removesAllFGrades(gradesList)
        # Quit Program.
        elif(choice == '7'):
            print()
            marquee("Thank You. Bye!")
        # If user enters anything else besides the given options they have to try again.
        else:
            print()
            marquee("Invalid Menu Selection. Try Again.")
            pause()

#----------------------------------------------------------------------------------------------

def getChoiceFromUserAfterDisplayMenu():

    # This is the main menu our user will see during the program.
    result = ''
    cls()
    marquee("    M A I N    M E N U     ")
    menu = "\n1. Add One Exam Score"
    menu += "\n2. Add Exam Scores Until User Enters -999"
    menu += "\n3. Display All Exam Scores"
    menu += "\n4. Display Exam Statistics"
    menu += "\n5. Adjust All Exam Scores"
    menu += "\n6. Remove All F Grades from GradeBook"
    menu += "\n7. Quit"
    menu += "\n"
    menu += "\nEnter Your Selection: "
    result = input(menu)

    return result

#----------------------------------------------------------------------------------------------

def getOneExamScore(gradesList):

    cls()
    marquee("Add an Exam Score in the Grade Book.")

    # Variables needed for lowest and highest number score.
    low = 0
    high = 100
    score = 555

    # Asks user for exam score and checks if the number is between the low and high boundaries.
    while(score < low or score > high):
        score = getInt("\nEnter an Exam Score: ")
        # If exam score inputted is below 0 or above 100 the user cannot proceed.
        if(score < low or score > high):
            print()
            mess = "You Must Enter an Exam Score Between " + str(low) + " and " + str(high) + "."
            marquee(mess)
            pause()
        # The exam score added by the user is put into our grade list.
        else:
            gradesList.append(score)
            print()
            marquee("A New Exam Score Has Been Added.")
            pause()

#----------------------------------------------------------------------------------------------

def getExamScoresTillValue(gradesList):

    print()
    marquee("Enter Exam Scores. Input -999 to Stop.")

    # Variables needed for low and high boundary, and exit boundary.
    low = 0
    high = 100
    stop = -999

    while(True):
        try:
            score = getInt("\nEnter an Exam Score: ")
            # 'break' allows you to exit a loop when an external condition is met.
            if(score == stop):
                break
            # If the score entered by user is between low and high boundaries, it is added to the list.
            elif(low <= score <= high):
                gradesList.append(score)
                print()
                marquee("Exam Score Added.")
            # If the user enters anything not between 0 and 100 we tell the user to try again.
            else:
                print()
                marquee(f"Invalid Score. Please Enter a Number Between {low} and {high}.")
                pause()
        except:
            print("You Must Enter a Valid Number.")

#----------------------------------------------------------------------------------------------

def displayAllExamScores(gradesList):

    choice = '100'

    while(choice != 'c'):
        choice = displayAllExamScoresMenu()
        # Displays exam scores from highest to lowest.
        if(choice == 'a'):
            displayAllExamScoresHighToLow(gradesList)
        # Displays exam scores from lowest to highest.
        elif(choice == 'b'):
            displayAllExamScoresLowToHigh(gradesList)
        # Allows the user to go back to the main menu.
        elif(choice == 'c'):
            getChoiceFromUserAfterDisplayMenu()
        else:
            print()
            marquee("Invalid Menu Selection. Try Again.")
            pause()

#----------------------------------------------------------------------------------------------

def displayAllExamScoresMenu():

    # This is the sub menu our user will see during the program.
    result = ''
    cls()
    marquee("    S U B    M E N U     ")
    menu = "\na. From Highest To Lowest"
    menu += "\nb. From Lowest To Highest"
    menu += "\nc. Go Back"
    menu += "\n"
    menu += "\nEnter Your Selection: "
    result = input(menu).lower()

    return result

#----------------------------------------------------------------------------------------------

def displayAllExamScoresHighToLow(gradesList):

    # If no exam scores are in our list, the program will tell the user this information.
    if (len(gradesList) == 0):
        print()
        marquee("There are No Grades to Show. Try Selection 1 or 2 in the Main Menu.")
        pause()
        return
    print()
    marquee("List of Grades")
    print()

    # This will sort the list in descending order (high to low).
    sortedGradeList = sorted(gradesList, reverse=True)

    # This creates a list of all grades stored in our list starting from 1.
    for i in range(len(gradesList)):
        score = sortedGradeList[i]
        letterGrade = calculateLetterGrade(score)
        print(f"{i + 1}. \t{score} \t{letterGrade}")
    pause()

#----------------------------------------------------------------------------------------------

def displayAllExamScoresLowToHigh(gradesList):

    # If no exam scores are in our list, the program will tell the user this information.
    if (len(gradesList) == 0):
        print()
        marquee("There are No Grades to Show. Try Selection 1 or 2 in the Main Menu.")
        pause()
        return
    print()
    marquee("List of Grades")
    print()

    # This will sort the list in ascending order (low to high).
    sortedGradeList = sorted(gradesList)

    # This creates a list of all grades stored in our list starting from 1.
    for i in range(len(gradesList)):
        score = sortedGradeList[i]
        letterGrade = calculateLetterGrade(score)
        print(f"{i + 1}. \t{score} \t{letterGrade}")
    pause()

#----------------------------------------------------------------------------------------------

def calculateLetterGrade(score):

    # Calculates the letter grade for each score.
    if(90 <= score <= 100):
        return 'A'
    elif(80 <= score < 90):
        return 'B'
    elif(70 <= score < 80):
        return 'C'
    elif(60 <= score < 70):
        return 'D'
    else:
        return 'F'

#----------------------------------------------------------------------------------------------

def displayExamStats(gradesList):

    # If no exam scores are in our list, the program will tell the user this information.
    if len(gradesList) == 0:
        marquee("There are No Grades to Show. Try Selection 1 or 2 in the Main Menu.")
        pause()
        return
    # If there is somthing in the list then the program will run and display the grade stats.
    else:
        marquee("Grade Statistics")
        print()
        print(f"Total Number of Grades: {str(len(gradesList))}")
        print()
        # Displays the highest grade.
        print("Highest Grade: " + str(max(gradesList)))
        # Displays the lowest grade.
        print("Lowest Grade.: " + str(min(gradesList)))
        # Displays the grade average.
        print("Grade Average: " + str((sum(gradesList) / len(gradesList))))
        print()

        # An empty list for all grades so that even if there is no grade for one of the sections the program will show 0.
        aGrades = []
        bGrades = []
        cGrades = []
        dGrades = []
        fGrades = []

        # Checks every number inside the list and puts it in the appropriate category.
        for i in gradesList:
            if(i >= 90):
                aGrades.append(i)
            elif(80 <= i <= 89):
                bGrades.append(i)
            elif(70 <= i <= 79):
                cGrades.append(i)
            elif(60 <= i <= 69):
                dGrades.append(i)
            else:
                fGrades.append(i)
        # Displays the grade statistics.
        print("There are " + str(len(aGrades)) + " grades that are A's.")
        print("There are " + str(len(bGrades)) + " grades that are B's.")
        print("There are " + str(len(cGrades)) + " grades that are C's.")
        print("There are " + str(len(dGrades)) + " grades that are D's.")
        print("There are " + str(len(fGrades)) + " grades that are F's.")
        pause()

#----------------------------------------------------------------------------------------------

def reducesAllExamScoresByFive(gradesList):

    # 'not' is an operator that negates the truth value of a statement.
    # In this context this statement simply checks whether the gradesList is empty.
    # If it is empty we will tell the user this information then bring them back to the main menu.
    cls()
    if(not gradesList):
        print()
        marquee("No Exam Scores to Reduce.")
    else:
        print("\nCurrent Scores \t New Scores")
        # 'enumerate' is a built-in function that iterates over a list while keeping track of the index.
        # 'i' represents the index number that holds each score.
        # We calculate the new score, and 'max(0' means the max limit the number can go down is 0.
        # 'gradesList[i] = newScore' essentially replaces the old index score with the new index score.
        for i, score in enumerate(gradesList):
            newScore = max(0, score - 5)
            print(f"{score}\t\t\t\t {newScore}")
            gradesList[i] = newScore
        print()
        marquee("All Exam Scores Have Been Reduced by 5 Points")
    pause()

#----------------------------------------------------------------------------------------------

def removesAllFGrades(gradesList):

    # If no exam scores are in our list, the program will tell the user this information.
    if (len(gradesList) == 0):
        print()
        marquee("There are No Grades to Show. Try Selection 1 or 2 in the Main Menu.")
        pause()
        return

    for grade in gradesList[:]:
        if(grade < 60):
            gradesList.remove(grade)
    print()
    marquee("All F Scores Have Been Removed From the GradeBook.")
    pause()
    return

#----------------------------------------------------------------------------------------------

def getInt(string):

    # This variable assumes the users input is invalid unless proven otherwise.
    badValue = True

    # The while loop ensures the user enters a floating point number.
    # The try and except makes sure a runtime error does not occur.
    # If the user does not enter a number, the loop will restart.
    while (badValue):
        try:
            value = int(input(string))
            badValue = False
        except:
            badValue = True
            print()
            marquee("You Must Enter a Valid Number.")
            pause()
    return value

#----------------------------------------------------------------------------------------------

def cls():

    # This clears the screen.
    print("\n" * 100)

#----------------------------------------------------------------------------------------------

def marquee(mess):

    # This function creates a unique border for whatever message we desire.
    symbol = '#'
    size = len(mess) + 6
    print(symbol * size)
    print(symbol * 2, mess, symbol * 2)
    print(symbol * size)

#----------------------------------------------------------------------------------------------

def pause():

    # This stops the program until the user press Enter on their keyboard.
    input("\nPress ENTER to Continue...")

main()