//=====================================================//
//=====================================================//
//== Written By.: AJ                                 ==//
//== Date Writen: February 23, 2024                  ==//
//== Purpose....: Median & Average Pass By Reference ==//
//=====================================================//
//=====================================================//

#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

// This function calculates the average, sorts the array, and calculates the median.
void passByMedianAndAverage(double values[], int size, double *pAverage, double *pMedian)
{
	// Variable needed to calculate the average by accumulating
	// the sum of all elements in the array.
	double sum = 0.0;

	// Calculating the average.
	// This 'for' loop iterates through each element in the array.
	for (int i = 0; i < size; i++)
	{
		sum += values[i];
	}
	// The result of this is stored in the memory location by this pointer.
	*pAverage = sum / size;

	// Sort the array using the bubble sort method.
	for (int i = 0; i < size - 1; i++)
	{
		for (int j = 0; j < size - i - 1; j++)
		{
			if (values[j] > values[j + 1])
			{
				double temp = values[j];
				values[j] = values[j + 1];
				values[j + 1] = temp;
			}
		}
	}

	// Calculate the median.
	// 'if' checks if size of array is even.
	if (size % 2 == 0)
	{
		// Due to the bubble sort, this accesses the value before the middle
		// and the value in the middle to calculate the median which is stored
		// in our median pointer.
		*pMedian = (values[size / 2 - 1] + values[size / 2]) / 2.0;
	}
	// 'else' checks if size of array is odd.
	else
	{
		// Due to the bubble sort, this accesses the middle value and
		// calculates the median which is stored in our median pointer.
		*pMedian = values[size / 2];
	}
}

int main()
{
	// Given array of data.
	double values[15] = { 7.7, 1001.2, 654.7, 12.8, 0.91, 15.102, 812.5, 121.6, 382.1,
						  40.1, 452.0, 128.2, 544.6, 23.2, 750.1 };

	// Variables needed for average and median. Will be used for pass by reference.
	double average;
	double median;

	// Call the 'passByMedianAndAverage' function that calculates the average and median. 
	// Putting the '&' reference operator in front of our variables so it can be stored
	// in the pointer which accesses the address. This is pass by reference.
	passByMedianAndAverage(values, 15, &average, &median);

	// Display the results.
	printf("Average: %.2f\n", average);
	printf("Median.: %.2f\n", median);

	return 0;
}