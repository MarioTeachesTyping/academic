//=======================================================//
//=======================================================//
//== Written By..: AJ                                  ==//
//== Date Written: January 30, 2024                   ==//
//== Purpose.....: Array Searcher for Particular Value ==//
//=======================================================//
//=======================================================//

#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

void main()
{
    // This is the array of values.
    int myBigArray[50] = { 6,39,37,70,47,53,84,42,6,95,56,19,90,7,70,99,70,
        44,23,52,42,82,40,17,33,12,62,55,24,74,60,84,47,87,59,90,91,10,
        62,91,27,63,62,55,79,56,91,38,98,60 };

    // These are the variables needed for our value and count.
    int value = 0;
    int count = 0;
    
    // This prompts the user to enter a value and sets it to the variable 'value'.
    printf("What Value do you Want to Search for? ");
    scanf("%i", &value);

    // This 'for' loop will iterate through each index in the array.
    for(int i = 0; i < 50; i++) 
    {
        // This 'if' statement checks if this value is in the array.
        if(value == myBigArray[i]) 
        {
            printf("Found %d at Index %d.\n", value, i);
            // This increments for each time the value is found.
            count++;
        }
    }

    // This 'if' statement checks if count is incremented 0 times.
    if(count == 0) {
        // This will inform the user that their value could not be found in the array.
        printf("Could Not Find %d in the Array.\n", value);
    }
}