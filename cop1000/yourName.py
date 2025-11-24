#####################################
## Written by: Anthony Terry (AJ)  ##
## Date Written: September 6, 2023 ##
## Purpose: Input & Output Name    ##
#####################################

def main():

    # This is where input our information.
    firstName = input("Enter your First Name: ")
    lastName = input("Enter your Last Name: ")
    count = int(input("Enter How Many Times you Want your Name to be Displayed: "))

    # Display the first and last name.
    for i in range(10):
        print(f"{(i + 1):3}. {firstName} {lastName}")

    # The start and stop points (f stands for format).
    count = i + 1
    stop = count + 5

    # Display the last and first name.
    for i in range(count,stop):
        print(f"{(i + 1):3}. {lastName} {firstName}")

main()