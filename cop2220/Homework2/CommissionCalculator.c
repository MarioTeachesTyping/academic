//==================================================================//
//==================================================================//
//== Written By..: AJ                                             ==//
//== Date Written: January 23, 2024                               ==//
//== Purpose.....: Commission Calculator for Sales Representative ==//
//==================================================================//
//==================================================================//

#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

// This indicates that the function should return an integer value.
int main()
{
	// Variables needed for users sales, commission percentages,
	// and total sales after commission calculation.
	int sales = 0;
	double commissions = 0.0;
	double totalCommissions = 0.0;

	// This will ask the user for their sales.
	printf("Enter the Sales Amount: ");
	scanf("%d", &sales);

	// If they made $5000 or less in sales they receive a 5% commission.
	if (sales <= 5000)
	{
		commissions = 0.05;
	}

	// If they made more than %5000 but less than or equal to $10,000,
	// they receive a 7.5% commission.
	else if (5000 < sales <= 10000)
	{
		commissions = 0.075;
	}

	// If they made more than $10,000 they receive a 9% commission.
	else if (sales > 10000)
	{
		commissions = 0.09;
	}

	// This performs the calculation to tell the user how much commission they got based on sales.
	totalCommissions = commissions * sales;

	// This outputs our commission we calculated to the user based on their sales.
	printf("Your Commission is: $%.2lf\n", totalCommissions);
}