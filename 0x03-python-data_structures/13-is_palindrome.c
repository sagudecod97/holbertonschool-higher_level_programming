#include "lists.h"

/**
 * is_palindrome - Function checks if singly linked list a palindrome
 * @head: Head of Linked list
 * Return: 0 not palindrome, 1 palindrome
 */

int is_palindrome(listint_t **head)
{
	int j = 0, length = 0, intPtr[9999], half = 0;
	listint_t *tmp = *head;

	if (!head || !tmp->next || !*head)
		return 1;

	while (tmp)
	{
		intPtr[length] = tmp->n;
		length++;
		tmp = tmp->next;
	};
	half = length - 1;
	while (j <= half)
	{
		if (intPtr[j] != intPtr[half])
		{
			return 0;
		}
		j++;
		half--;
	};
	return (1);
}
