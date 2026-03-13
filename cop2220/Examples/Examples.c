#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>

typedef struct node
{
	int data;
	struct node* next;
}node;

node* create_node(int item)
{
	node* temp = malloc(sizeof(node));
	temp->data = item;
	temp->next = NULL;
	return temp;
}

// this function takes an item and insert it in the linked list pointed by root.
node* insert_front(node* head, int item)
{
	// create the box for node
	node* temp = create_node(item);

	// we need to insert this node at the beginning of the list
	if (head == NULL)
	{
		head = temp; // this will not change the original head
		return head;
	}
	else
	{
		temp->next = head;
		head = temp;
		return head;
	}
}

// This function takes an item and sorts it in the linked list.
node* insert_sorted(node* head, int item)
{
	// Could just call 'create_node' but this is if you cant.
	node* temp = malloc(sizeof(node));

	temp->data = item;
	temp->next = NULL; // for standard practice put null. figure out if pointer later.

	// without 'head == NULL' the code will crash if nothings in the list yet.
	// if 'head == NULL' isnt first the code will crash cause it wont check if the list is null.
	if (head == NULL || item < head->data)
	{
		temp->next = head;
		head = temp;
		return head;
	}
	else
	{
		node* walker = head;
		
		// if next item is not null and smaller than walker. walker takes it spot.
		// while loop cause it checks through each item in the list before breaking.
		while (walker->next != NULL && walker->next->data < item)
		{
			walker = walker->next;
		}

		temp->next = walker->next;
		walker->next = temp;
	}

	return head;
}

// This function takes an item and insert it in the end of the linked list.
node* insert_end(node* head, int item)
{
	node* temp = create_node(item);

	// if there's nothing. then it's the new head.
	if (head == NULL)
	{
		head = temp;
		return head;
	}
	else
	{
		node* walker = head;

		// if walker finds null the loop will end
		while (walker->next) // same as walker->next !=NULL
		{
			walker = walker->next;
		}

		// if you are here, it means you are the last node of the list.
		walker->next = temp;
		return head;
	}
}


/*
this function deletes the first occurrence of a given item from linked list.
it returns the updated/original root
*/
node* DelList(node* head, int item)
{

}

void display(node* t)
{
	printf("\nPrinting your linked list.......");

	while (t != NULL)
	{
		printf("%d ", t->data);
		t = t->next;
	}

	printf("\n");

}

int main()
{
	// NULL is mandatory for this line.
	node* root = NULL;

	// declare root appropriately

	int ch, ele, v, del;

	while (1)
	{
		printf("\nMenu: 1. insert at the front, 2. insert at the end, 3. Delete, 5.  sorted insert 4. exit: ");
		scanf("%d", &ch);
		if (ch == 4)
		{
			printf("\nGOOD BYE>>>>\n");
			break;
		}
		if (ch == 1)
		{
			printf("\nEnter data(an integer): ");
			scanf("%d", &ele);

			// call the function appropriately 
			display(root);
		}
		if (ch == 2)
		{
			printf("\nEnter information(an integer): ");
			scanf("%d", &ele);

			// call the function appropriately 
			display(root);

		}
		if (ch == 3)
		{
			printf("\nEnter info which u want to DELETE: ");
			scanf("%d", &del);

			// call the function appropriately
			display(root);
		}

		if (ch == 5)
		{
			printf("\nEnter data(an integer): ");
			scanf("%d", &ele);

			// call appropriately  
			display(root);
		}
	}
	return 0;
}