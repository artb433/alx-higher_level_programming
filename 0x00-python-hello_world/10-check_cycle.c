#include <stdio.h>
#include "lists.h"

/**
 * check_cycle - check if a linked list has cycles
 *
 * @list: head of linked list
 *
 * Return: 0 if there are no cycles; otherwise 1
 */

int check_cycle(listint_t *list)
{
	listint_t *temp, *iter;

	if (list == NULL)
		return (0);

	temp = list;
	iter = list;

	while (iter->next != NULL)
	{
		iter = iter->next;

		if (iter == temp)
			return (1);
	}

	return (0);
}
