#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

void no(void)
{
  puts("Nope.");
  exit(1);
}

void ok(void)
{
  puts("Good job.");
  return;
}

typedef struct s_ascii_val
{
	char a;
	char b;
	char c;
	char d;
} ascii_val;


int main(void)
{
  int temp_pos;
  int digit_val;
  size_t decoded_len;
  bool breaK_loop;
  ascii_val asc;
  char input[31];
  char decrypted[9];
  int input_pos;
  int diff;
  int decoded_index;
  int did_scanf_work;
  int useless;
  
  useless = 0;
  asc.d = '\0';
  printf("Please enter key: ");
  did_scanf_work = scanf("%23s",input);
  if (did_scanf_work != 1)
	no();
  if (input[1] != '2')
	no();
  if (input[0] != '4')
	no();
  fflush(stdin);
  memset(decrypted,0,9);
  decrypted[0] = '*';
  input_pos = 2;
  decoded_index = 1;
  while( true ) {
	decoded_len = strlen(decrypted);
	temp_pos = input_pos;
	breaK_loop = false;
	if (decoded_len < 8) {
	  decoded_len = strlen(input);
	  breaK_loop = temp_pos < decoded_len;
	}
	if (!breaK_loop) break;
	asc.a = input[temp_pos];
	asc.b = input[temp_pos + 1];
	asc.c = input[temp_pos + 2];
	digit_val = atoi(&asc.a);
	decrypted[decoded_index] = (char)digit_val;
	input_pos = input_pos + 3;
	decoded_index = decoded_index + 1;
  }
  decrypted[decoded_index] = '\0';
  diff = strcmp(decrypted,"********");
  if (diff == 0)
	ok(); // Good job.
  else
	no(); // Nope.
  return 0;
}