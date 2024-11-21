#include <stdio.h>
#include <string.h>

int	main(void)

{
	const char password[] = "__stack_check";
	char input_buffer[64];
	int diff;

	printf("Please enter key: ");
	scanf("%s", input_buffer);
	diff = strcmp(input_buffer, password);
	if (diff == 0)
	{
		printf("Good job.\n");
	}
	else
	{
		printf("Nope.\n");
	}
	return (0);
}
