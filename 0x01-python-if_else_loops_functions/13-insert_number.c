#include "lists.h"
#include <stdio.h>

/**
 * insert_node -  inserts a number into a sorted singly linked list
 * @head:  double pointer to the head of the list
 * @num: the number to insert as new node
 * Return: pointer to new node or NULL on failure
 */
listint_t *insert_node(listint_t **head, int num)
{
	listint_t *new, *before, *curr;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	/*else*/
	new->n = num;
	/*Determine where to insert new in list*/
	curr = *head;
	if (curr == NULL)
	{
		new->next = curr;
		*head = new;
	}
	else if (curr->n > num)
	{
		new->next = curr;
		*head = new;
	}
	else
	{
		for (; curr != NULL && curr->n < num; curr = curr->next)
			before = curr;
		before->next = new;
		new->next = curr;
	}
	return (new);
}

