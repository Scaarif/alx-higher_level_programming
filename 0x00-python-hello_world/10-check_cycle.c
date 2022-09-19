#include "lists.h"
#include <stdio.h>
#include <stddef.h>

/**
 * check_cycle - detects presence of a loop in a list
 * @list: the list to check
 * Return: 1 if loop and 0 otherwise
 */
int check_cycle(listint_t *list)
{
	listint_t *S = list, *F = list;

	while (S && F && F->next) /*as long as none of these are NULL*/
	{
		S = S->next;/*move forward a node*/
		F = F->next->next;/*move forward 2 nodes*/
		if (S == F)
			return (1);/*if true*/
	}
	return (0);/*if false*/
}
