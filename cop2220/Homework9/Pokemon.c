//==================================//
//==================================//
//== Written By..: AJ             ==//
//== Date Written: April 17, 2024 ==//
//== Purpose.....: Pokemon Stats  ==//
//==================================//
//==================================//

#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>

typedef struct
{
    char name[100];
    int level;
    int hp;
    int attackPower;
} Pokemon;

Pokemon* CreateArray(FILE* fp, int* pN)
{
    int n;
    Pokemon* newArray;

    // Use fscanf to read the next integer from the file fp and save it to n.
    fscanf(fp, "%d", &n);
    // Set pN equal to n (remember that pN is a pointer).
    *pN = n;
    // Use calloc to set newList to a dynamically allocated array of size n and data type Pokemon.
    newArray = (Pokemon*)calloc(n, sizeof(Pokemon));

    return newArray;
}

Pokemon ReadNextPokemon(FILE* fp)
{
    Pokemon newPokemon;

    // Using fscanf read a STRING from the file fp and save it to the name component of newPokemon.
    fscanf(fp, "%s", newPokemon.name);
    // Using fscanf read an INT from the file fp and save it to the level component of newPokemon.
    fscanf(fp, "%d", &newPokemon.level);
    // Using fscanf read an INT from the file fp and save it to the hp component of newPokemon.
    fscanf(fp, "%d", &newPokemon.hp);
    // Using fscanf read an INT from the file fp and save it to the attackPower component of newPokemon.
    fscanf(fp, "%d", &newPokemon.attackPower);

    return newPokemon;
}

void PrintPokemon(Pokemon* pokemonArray, int size)
{
    // Make a for loop that goes from 0 to size.
    // Inside the for loop print each component of pokemonArray[i] using printf-
    // this includes the name, level, HP and attack power.
    for (int i = 0; i < size; i++)
    {
        printf("Name: %s\n", pokemonArray[i].name);
        printf("Level: %d\n", pokemonArray[i].level);
        printf("HP: %d\n", pokemonArray[i].hp);
        printf("AP: %d\n", pokemonArray[i].attackPower);
    }
}

void FreeArray(Pokemon* pokemonArray)
{
    // Free the dynamically allocated pokemonArray.
    free(pokemonArray);
}

void main()
{
    Pokemon* pokemonList;
    int arraySize;
    FILE* fp;

    // Using fopen, open the pokemondata.txt file for read only access.
    fp = fopen("pokemondata.txt", "r");

    pokemonList = CreateArray(fp, &arraySize);

    // Create a for loop that goes from 0 to arraySize.
    // Inside the for loop set pokemonList[i] to the structure returned by ReadNextPokemon(fp).
    for (int i = 0; i < arraySize; i++)
    {
        pokemonList[i] = ReadNextPokemon(fp);
    }

    // Call PrintPokemon with the parameters pokemonList and arraySize.
    PrintPokemon(pokemonList, arraySize);

    // Call FreeArray with the parameter pokemonList.
    FreeArray(pokemonList);

    // Close the file fp that you opened in the line above.
    fclose(fp);
}