#include "lists.h"
#include <stdio.h>
#include <stddef.h>

/**
 * check_cycle - detects presence of a loop in a list
 * @list: pointer to the head of the list to check
 * Description: two trackers are used, a Fast(F) and Slow(S)
 * moving nodes. If the nodes ever meet (i.e. are equal at a
 * point during the movement, then a cycle exists in the list
 * - logically, since F moves 2 nodes at a time while S moves
 *   only a node at a time)
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
