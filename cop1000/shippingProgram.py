##########################################
## ************************************ ##
## * Written By..: Anthony Terry (AJ) * ##
## * Date Written: October 27, 2023   * ##
## * Purpose.....: Shipping Program   * ##
## ************************************ ##
##########################################

def main():

    displayShippingProgram()

#----------------------------------------------------------------

def cDistanceCost(distance):

    # Calculate the distance cost based on how many miles away it is.
    # If the distance is equal to or less than 250 miles, the cost of $15.00 is added to the total cost.
    # If the distance is greater than 250 miles, $15.00 is added for every 250 miles of the total distance.
    cost = (distance // 250) * 15

    if(distance % 250 != 0):
        cost += 15
    return cost

#----------------------------------------------------------------

def cFragileCost(fragile, weightCost):

    # Calculate the fragility cost based on if the package is fragile or not.
    # If the package is fragile, we add $2.00 to the cost based on the weight.
    if(fragile == "yes"):
        return weightCost + 2.00
    else:
        return 0.0

#----------------------------------------------------------------

def cWeightCost(weight):

    # Calculate the weight cost based on how many pounds the package weighs.
    # If the package is equal to or less than 10 pounds, the cost is $3.75.
    # If the package is greater than 10 pounds, then the cost is $3.75 + $0.50 based on each pound of over 10.
    if(weight <= 10):
        cost = 3.75
    else:
        extraWeight = weight - 10
        cost = 3.75 + (0.5 * extraWeight)
    return cost

#----------------------------------------------------------------

def displayShippingProgram():

    # Displays a welcome message.
    marquee("Thank You for Choosing Our Shipping Program!")

    # The user enters the specific responses needed for each question.
    # '.lower() converts the input for fragility to lowercase.
    weight = float(input("Enter How Much the Package Weighs (In Pounds): "))
    distance = int(input("Enter the Distance of the Package (In Miles).: "))
    fragile = input("Is the Package Fragile? (Yes/No).............: ").lower()

    # The cost for each question based on the user's answer and total cost of package.
    weightCost = cWeightCost(weight)
    distanceCost = cDistanceCost(distance)
    fragileCost = cFragileCost(fragile, weightCost)
    totalCost = weightCost + distanceCost + fragileCost

    print("▫▫▫▫▫▫▫▫▫▫▫▫▫▫▫▫▫▫▫▫▫▫▫▫▫▫▫▫▫▫▫▫▫▫▫▫▫▫▫▫▫▫▫▫▫▫▫▫▫▫")
    print(f"The Cost to Ship Based on Weight..: ${weightCost:.2f}")
    print(f"The Cost to Ship Based on Distance: ${distanceCost:.2f}")
    print(f"The Total Shipping Cost...........: ${totalCost:.2f}")
    print("▫▫▫▫▫▫▫▫▫▫▫▫▫▫▫▫▫▫▫▫▫▫▫▫▫▫▫▫▫▫▫▫▫▫▫▫▫▫▫▫▫▫▫▫▫▫▫▫▫▫")

#----------------------------------------------------------------

def marquee(mess):

    # Creates a unique border for any 'print()' we want.
    print(" ")
    symbol = '▫'
    size = len(mess) + 6
    print(symbol * size)
    print(symbol * 2, mess, symbol * 2)
    print(symbol * size)

main()