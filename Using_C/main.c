#include "main.h"

/**
 * main - Entry Point
 * @ac: number of argument
 * @av: Content of argument
 *
 * Return: 0 when success
 */
int main(int ac, char *av[])
{
	FILE *file;

	if (ac != 2)
	{
		fprintf(stderr, "USAGE factors file\n");
		exit(EXIT_FAILURE);
	}
	file = fopen(av[1], "r");
	if (file == NULL)
	{
		fprintf(stderr, "Can't open file %s\n", av[1]);
		exit(EXIT_FAILURE);
	}
	read_file(file);

	fclose(file);
	return (0);
}
