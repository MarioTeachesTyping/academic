##########################################
## ************************************ ##
## * Written By..: Anthony Terry (AJ) * ##
## * Date Written: November 8, 2023   * ##
## * Purpose.....: Disney Election    * ##
## ************************************ ##
##########################################

def main():

    choice = '100'
    # This will hold our votes for Mickey and Minnie.
    mickeyList = []
    minnieList = []
    while(choice != 'E'):
        choice = getChoiceFromUserAfterDisplayMenu()
        # Get votes for Mickey and Minnie from user.
        if(choice == 'A'):
            addVotesFromAPrecinct(mickeyList, minnieList)
        # Display votes for Mickey and Minnie for each precinct.
        elif(choice == 'B'):
            displayAllVotes(mickeyList, minnieList)
        # Display highest, lowest, and average amount of votes for Mickey and Minnie.
        elif(choice == 'C'):
            displayVoteStats(mickeyList, minnieList)
        # Get user to remove a precinct which will remove all votes from that precinct.
        elif(choice == 'D'):
            removeAPrecinct(mickeyList, minnieList)
        # Quit Program.
        elif(choice == 'E'):
            print()
            marquee("Bye!")
        else:
            print()
            marquee("Invalid Menu Selection. Try Again.")
            pause()

#----------------------------------------------------------------------------------------------

def addVotesFromAPrecinct(mickeyList, minnieList):

    # This will take the users input for votes in a precinct and store them to those lists.
    cls()
    marquee("Add Any Amount of Votes for Both Candidates.")
    print()
    mickeyList.append(getInt("Enter the Votes for Mickey Mouse in this Precinct: "))
    minnieList.append(getInt("Enter the Votes for Minnie Mouse in this Precinct: "))
    print()
    marquee("The Votes Have Been Added.")
    pause()

#----------------------------------------------------------------------------------------------

def cls():

    # Creates an empty space.
    print("\n" * 100)

#----------------------------------------------------------------------------------------------

def displayAllVotes(mickeyList, minnieList):

    # If no votes are in our list, the program will tell the user this information.
    if(len(mickeyList) == 0):
        print()
        marquee("You Must Enter at Least One Precinct First. Add Votes in Selection A.")
        pause()
        return
    cls()
    marquee("All Precincts Votes for the New Candidates.")
    print()
    # This displays information telling the user what each section represents.
    print(f"Precinct \t    Mickey   \tMinnie")
    # The '{i + 1}' ensures our precincts start from 1 since indexes start from 0.
    # The ': 3' after is used to right align the value (i + 1) in 3 spaces of width.
    # If i is 0 {i + 1: 3} will be '  1' and if i is 9 {i + 1: 3} will be ' 10'.
    # Doing this ensures the formatting of the precinct numbers and votes are neat.
    for i in range(len(mickeyList)):
        print(f"\t{i + 1: 3}. \t{mickeyList[i]:10,}\t{minnieList[i]:10,}")
    pause()

#----------------------------------------------------------------------------------------------

def displayVoteStats(mickeyList, minnieList):

    # If no votes are in our list, the program will tell the user this information.
    if(len(mickeyList) == 0):
        print()
        marquee("You Must Enter at Least One Precinct First. Add Votes in Selection A.")
        pause()
        return

    # These variables calculate the highest, lowest, and average amount of votes for Mickey and Minnie.
    highestVotesMickey = max(mickeyList)
    lowestVotesMickey = min(mickeyList)
    averageVotesMickey = sum(mickeyList) / len(mickeyList)
    highestVotesMinnie = max(minnieList)
    lowestVotesMinnie = min(minnieList)
    averageVotesMinnie = sum(minnieList) / len(minnieList)

    # This will display our results for highest, lowest, and average amount of votes.
    cls()
    marquee("Voting Statistics")
    print()
    print(f"☆ Mickey Mouse ☆")
    print(f"Highest Number of Votes From One Precinct.: ", f"{highestVotesMickey:.0f}")
    print(f"Lowest Number of Votes From One Precinct..: ", f"{lowestVotesMickey:.0f}")
    print(f"Average Number of Votes From All Precincts: ", f"{averageVotesMickey:.0f}")
    print()
    print(f"☆ Minnie Mouse ☆")
    print(f"Highest Number of Votes From One Precinct.: ", f"{highestVotesMinnie:.0f}")
    print(f"Lowest Number of Votes From One Precinct..: ", f"{lowestVotesMinnie:.0f}")
    print(f"Average Number of Votes From All Precincts: ", f"{averageVotesMinnie:.0f}")
    pause()

#----------------------------------------------------------------------------------------------

def getChoiceFromUserAfterDisplayMenu():

    # This is the menu our user will see during the program.
    result = ''
    cls()
    marquee("    M A I N    M E N U     ")
    menu = "\n☆ A. Add Votes From a Precinct"
    menu += "\n☆ B. Display All Votes From All Precincts"
    menu += "\n☆ C. Display Vote Stats"
    menu += "\n☆ D. Remove a Precinct and All Votes From that Precinct"
    menu += "\n☆ E. Quit"
    menu += "\n"
    menu += "\nEnter Your Selection: "
    result = input(menu).upper()

    return result

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
            print()
    return value

#----------------------------------------------------------------------------------------------

def marquee(mess):

    # This function creates a unique border for whatever message we desire.
    symbol = '+'
    size = len(mess) + 6
    print(symbol * size)
    print(symbol * 2, mess, symbol * 2)
    print(symbol * size)

#----------------------------------------------------------------------------------------------

def pause():

    # This stops the program until the user press Enter on their keyboard.
    input("\nPress ENTER to Continue...")

#----------------------------------------------------------------------------------------------

def removeAPrecinct(mickeyList, minnieList):

    # If no votes are in our list, the program will tell the user this information.
    if(len(mickeyList) == 0):
        print()
        marquee("You Must Enter at Least One Precinct First. Add Votes in Selection A.")
        pause()
        return
    # This will ask the user to remove a precinct and the votes associated with that precinct.
    # We will display our precincts and votes beforehand to show the user what they can remove.
    cls()
    displayAllVotes(mickeyList, minnieList)
    print()
    marquee("Remove a Precinct and All Votes From that Precinct.")
    print()

    # This variable is used to get the number the user wants associated with that precinct.
    precinctToRemove = getInt("Enter the Precinct Number to Remove: ")

    # This ensures the users number isn't below 1 or above the amount of precincts shown.
    if(precinctToRemove < 1 or precinctToRemove > len(mickeyList)):
        print()
        marquee("Invalid Precinct Number.")
        pause()
        return

    # del is used to delete any objects which include variables, lists, parts of a list, etc.
    # We use del here to remove any elements from the index chosen by the user from Mickey and Minnie's list.
    # The '- 1' modifies the list and reduces the length of Mickey and Minnie's list by 1.
    del mickeyList[precinctToRemove - 1]
    del minnieList[precinctToRemove - 1]

    # This tells the user the program has removed the precinct and it's votes.
    print()
    marquee(f"Precinct {precinctToRemove} and it's Votes Have Been Removed.")
    pause()

main()