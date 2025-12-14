//==================================//
//==================================//
//== Written By..: AJ             ==//
//== Date Written: March 14, 2024 ==//
//== Purpose.....: Dog Struct     ==//
//==================================//
//==================================//

#include <stdio.h>

// Created our own data type for our struct Dog.
// A struct essentially holds variables in it's own data type.
typedef struct
{
	char name[50];
	char breed[50];
	char addressLine1[100];
	char addressLine2[100];
}Dog;

// This function creates a dog by getting user input.
Dog createDog()
{
	Dog newDog;

	// 'gets()' is used to read strings.
	printf("Enter the Dog's Name: ");
	gets(newDog.name);

	printf("Enter the Dog's Breed: ");
	gets(newDog.breed);

	printf("Enter the First Address Line: ");
	gets(newDog.addressLine1);

	printf("Enter the Second Address Line: ");
	gets(newDog.addressLine2);

	return newDog;
}

// This function prints the dog's information.
// The 'const' keyword prevents a variable from being changed.
void displayDog(const Dog *dog)
{
	// When accessing a pointer to a struct '->' is required.
	printf("\nThe Dog's Name is %s and their Breed is a %s.\n", dog->name, dog->breed);
	printf("Their Home Resides in %s, %s.\n", dog->addressLine1, dog->addressLine2);
}

int main()
{
	// Creates a Dog struct variable.
	Dog myDog;

	// Dog struct variable is filled with user data on dog.
	myDog = createDog();

	// Prints the dog's information.
	displayDog(&myDog);

	return 0;
}