#include "lists.h"
#include <stdio.h>

/**
 * is_palindrome - checks if a list is a palindrome
 * @head: double pointer to the list head
 * Return: 1 if a palindrome and 0 otherwise
 */
int is_palindrome(listint_t **head)
{
	int len = 1, half_l;
	listint_t *curr, *tail, *before;

	/*If list is empty, return 1*/
	if (*head == NULL)
		return (1);
	/*Get the length and tail of the list*/
	for (tail = *head; tail->next != NULL; tail = tail->next, len++)
		;
	/*printf("tail: %d & len: %d\n", tail->n, len);*/
	/*Determine if a non-empty list is a palindrome*/
	half_l = len / 2;
	curr = *head;
	while (half_l > 1)
	{
		if (curr->n != tail->n)
			return (0);
		curr = curr->next;
		for (before = curr; before->next != tail; before = before->next)
			;
		/*printf("before: %d\n", before->n);*/
		tail = before;
		half_l--;
		/*printf("half_l: %d\n", half_l);*/
	}
	return (1);
}

