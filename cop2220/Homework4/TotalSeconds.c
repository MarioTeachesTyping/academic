//============================================//
//============================================//
//== Written By..: AJ                       ==//
//== Date Written: February 16, 2024        ==//
//== Purpose.....: Convert To Total Seconds ==//
//============================================//
//============================================//

#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

// This function converts the users hours, minutes, and seconds into total seconds.
int calculateTotalSeconds(int hours, int minutes, int seconds)
{
	// Variable needed for calculating total seconds.
	int totalSeconds = 0;

	// Every hour is 3600 seconds. Add that to total seconds.
	totalSeconds += hours * 3600;

	// Every minute is 60 seconds. Add that to total seconds.
	totalSeconds += minutes * 60;

	// Every second is added to total amount of seconds.
	totalSeconds += seconds;

	return totalSeconds;
}

int main()
{
	// Variables needed for hours, minutes, and seconds.
	int hours;
	int minutes;
	int seconds;

	// Prompt the user for how many hours, minutes, and seconds.
	printf("How Many Hours? ");
	scanf("%d", &hours);
	printf("How Many Minutes? ");
	scanf("%d", &minutes);
	printf("How Many Seconds? ");
	scanf("%d", &seconds);
	printf("\n");

	// Passing the 'calculateTotalSeconds' function to this variable.
	int totalSeconds = calculateTotalSeconds(hours, minutes, seconds);

	// Display the total seconds to the user.
	printf("That is %d Total Seconds.\n", totalSeconds);

	return 0;
}