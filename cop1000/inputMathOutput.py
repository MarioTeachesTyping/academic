##########################################
## ************************************ ##
## * Written By: Anthony Terry (AJ)   * ##
## * Date Written: September 23, 2023 * ##
## * Purpose: Input Math Output       * ##
## ************************************ ##
##########################################

def main():

    print("\n" * 10)
    favNumber = int(input("Enter Your Favorite Number....: "))

    while True:
        multiplier = int(input("Enter a Number Between 1 and 5: "))
        if(1 <= multiplier <= 5):
            break
        else:
            print("\nPlease Enter a Number Between 1 and 5!")

    print("\nYour Favorite Number is....................................:", favNumber)
    print("Your Favorite Number Times Multiplier......................:", favNumber * multiplier)
    print(f"Your Favorite Number Float Divided by Multiplier...........: {favNumber / multiplier:,.2f}")
    print(f"Your Favorite Number Integer Divided by Multiplier.........: {favNumber / multiplier:,.0f}")
    print(f"The Remainder of Your Favorite Number Divided by Multiplier: {favNumber % multiplier:,.0f}")

main()