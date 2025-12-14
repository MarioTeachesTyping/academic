//===============================================//
//===============================================// 
//== Written By..: AJ                          ==//
//== Date Written: February 23, 2024           ==//
//== Purpose.....: Decimal to Binary Algorithm ==//
//===============================================//
//===============================================//

#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

// This function converts a decimal to a binary number and outputs it.
void decimalToBinary(unsigned int n)
{
	// Start with an exponent of 128 because it's the highest bit in
	// an 8-bit binary number.
	unsigned int exponent = 128;

	printf("Binary Output.: ");

	// Loops through each bit in the binary representation.
	while (exponent >= 1)
	{
		// If the current bit is greater than or equal to
		// the exponent, print 1.
		if (n >= exponent)
		{
			printf("1");
			// This updates 'n' to remove the contribution
			// of the current bit.
			n = n - exponent;
		}
		else
		{
			// If the current bit is less than the exponent, print 0.
			printf("0");
		}
		// This moves to the next lower bit position.
		// (128 --> 64 --> 32 --> 16 --> 8...)
		exponent = exponent / 2;
	}
	printf("\n");
}

int main()
{
	// 'unsigned int' is always non-negative (zero or positive)
	// and can store bigger data values than signed int's.
	unsigned int input;

	// Prompt the user to enter a number.
	printf("Enter a Number: ");
	scanf("%u", &input);

	// Calling the 'decimalToBinary' function.
	decimalToBinary(input);

	return 0;
}