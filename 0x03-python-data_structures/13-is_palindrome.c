#include "lists.h"

/**
 * is_palindrome - Function checks if singly linked list a palindrome
 * @head: Head of Linked list
 * Return: 0 not palindrome, 1 palindrome
 */

int is_palindrome(listint_t **head)
{
	int i = 0, j = 0, length = 1, check = 1;
	int intPtr[1024], half = 0;
	listint_t *tmp;

	tmp = *head;
	while (tmp->next)
	{
		intPtr[i] = tmp->n;
		length++;
		tmp = tmp->next;
		i++;
	};
	intPtr[i] = tmp->n;
	half = length;
	if (length % 2 != 0)
		half = (length + 1) / 2;
	while (j <= half)
	{
		if (intPtr[j] == intPtr[length - 1])
		{
			j++;
			length--;
			continue;
		} else if (j == half && intPtr[j] == intPtr[length - 1])
			break;
		check = 0;
		break;
	};

	return (check);
}
