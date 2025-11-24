########################################
## ********************************** ##
## * Written By: Anthony Terry (AJ) * ##
## * Date Written: October 1, 2023  * ##
## * Purpose: Menu                  * ##
## ********************************** ##
########################################

def main():

    choice = 999

    # All the choices our user can make that will take them to different functions.
    while(choice !=4):
        choice = menu()
        if(choice == 1):
            name()
            input("\nPress ENTER to Continue.")
        elif(choice == 2):
            age()
            input("\nPress ENTER to Continue.")
        elif(choice == 3):
            date()
            input("\nPress ENTER to Continue.")
        elif(choice == 4):
            print("\nThank you for playing!")
            input("\nPress ENTER to Continue.")
        else:
            print("\nInvalid Choice. Choose from Selection Provided.")
            input("\nPress ENTER to Continue.")

#----------------------------------------------------------------------------

def menu():

    # This will be the menu the user sees when asked to select a choice.
    print("\n" * 10)
    print("-------------")
    print("-- 1. Name --")
    print("-- 2. Age  --")
    print("-- 3. Date --")
    print("-- 4. Quit --")
    print("-------------")

    result = int(input("\nChoose Selection: "))
    return result

#----------------------------------------------------------------------------

def name():

    # We will ask for the users name.
    getName = input("\nWhat is your Name: ")

    # We will display the users name in a sentence of our choice.
    print("\nYo", getName, ", I hope you have a nice day.")

#----------------------------------------------------------------------------

def age():

    # We will ask for the users age.
    getAge = int(input("\nHow Old are you: "))

    # We will display different sentences based on the age of our user.
    if(getAge >= 0 and getAge <= 18):
        print("\nYour", getAge, "? You should go to bed.")
    elif(getAge >= 19 and getAge <= 40):
        print("\nSince your", getAge, "we should go on a date.")
    elif(getAge >= 41 and getAge <= 115):
        print("\nJesus Christ.", getAge, "is old...")
    else:
        print("\nInvalid Age. That's impossible, put your actual age.")
        age()

#----------------------------------------------------------------------------

def date():

    # This is how we get our current date and time.
    from datetime import date

    # This specifies how we want our date and time to look when displayed to the user.
    today = date.today()
    calendarDate = today.strftime("%B %d, %Y")

    # We will display the date to the user using a simple sentence.
    print("\nToday's Date is", calendarDate)

main()