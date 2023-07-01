#include "main.h"

/**
 * read_file - read file line by line
 * @file: file want to read
 * Return: void
 */
void read_file(FILE *file)
{
	char *line = NULL;
	size_t len = 0;
	ssize_t nread;

	while ((nread = getline(&line, &len, file)) != -1)
	{
		print_output(atoi(line));
	}
	free(line);
}

/**
 * print_output - Output format: n=p*q
 * @n: Number that will convert to p * q
 * Return: void
 */
void print_output(long n)
{
	long i;

	for (i = 2; i < n; i++)
	{
		if (n % i == 0)
		{
			printf("%ld=%ld*%ld\n", n, n / i, i);
			break;
		}
	}
}
