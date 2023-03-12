#include "lists.h"
#include <stdio.h>
#include <stdlib.h>

/**
 * is_palindrome - check if the contents of a
 *                 linked list is a palindrome
 *
 * @head: head to linked list
 *
 * Return: 0 if linked list is not a palindrome
 *         1 if linked list is a palindrome
 */

int is_palindrome(listint_t **head)
{
	listint_t *temp;
	int i, list_len, *val_list, *rev_list, check, check2, iter;

	if (*head == NULL)
		return (1);

	check = list_len = 0;
	temp = *head;

	while (temp != NULL)
	{
		list_len += 1;
		temp = temp->next;
	}

	temp = *head;
	check2 = list_len;
	iter = list_len - 1;
	val_list = malloc(sizeof(int) * list_len);
	rev_list = malloc(sizeof(int) * list_len);

	for (i = 0; temp != NULL; i++) /*assign val in list to array val_list*/
	{
		val_list[i] = temp->n;
		temp = temp->next;
	}
	for (i = 0; i < list_len; i++) /*reverse list; assign val to rev_list*/
	{
		rev_list[i] = val_list[iter];
		iter--;
	}
	for (i = 0; val_list[i]; i++) /*check if rev_list == val_list*/
		if (val_list[i] == rev_list[i])
			check += 1;
	free(val_list);
	free(rev_list);
	if (check == check2)
		return (1);

	return (0);
}
