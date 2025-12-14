//=======================================================//
//=======================================================//
//== Written By..: AJ                                  ==//
//== Date Written: April 3, 2024                       ==//
//== Purpose.....: Dynamically Allocated List of Names ==//
//=======================================================//
//=======================================================//

#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef char* string;

// This function goes through an array of strings and prints them to the screen.
void PrintList(string pArray[], int size)
{
	printf("\nThese are the Names in the List:\n");

	for (int i = 0; i < size; i++)
	{
		printf("%s\n", pArray[i]);
	}
}

void main()
{
	string* pStringArray; // The array of strings we are dynamically allocating.
	int numberOfNames;    // The count of how many names the user intends to enter.
	char buffer[1000];    // A temporary buffer that stores the names as they are being entered.

	// Using scanf, read in how many names the user will enter, save to numberOfNames variable.
	printf("How Many Names Will You Enter: ");
	scanf("%d", &numberOfNames);

	// Dynamically allocate pStringArray using calloc or malloc (I recommend using calloc).
	// It should be an array of the string data type and uses numberOfNames as the count.
	pStringArray = (string*)calloc(numberOfNames, sizeof(string));

	for (int i = 0; i < numberOfNames; i++)
	{
			printf("Enter a Name: ");
			scanf("%s", &buffer);

			// Dynamically allocate pStringArray[i] using malloc.
			// The number of bytes will be strlen(buffer) + 1.
			pStringArray[i] = (string*)malloc(strlen(buffer) + 1);

			// Copy the buffer to pStringArray[i] using strcpy.
			strcpy(pStringArray[i], buffer);
	}

	// Call 'PrintList' to display the entered names.
	PrintList(&pStringArray[0], numberOfNames);

	for (int i = 0; i < numberOfNames; i++)
	{
		// Inside this loop free pStringArray[i].
		free(pStringArray[i]);
	}

	// After the loop free pStringArray itself.
	free(pStringArray);

	return 0;
}