#include <stdio.h>

int count_ones( int val );
void print_bits( int val );
int count_zeros( int val );
char most_frequent_symbol(char *file_name);
void negative_file(char *input_file_name, char *output_file_name);

int main (void)
{
	int value = 112233;
	char pt_file[] = "input/ListaPalavrasPT.txt";
    char encrypted_pt[] = "output/ListaPalavrasPTencrypted.txt";
    char decrypted_pt[] = "output/ListaPalavrasPTdecrypted.txt";

	char en_file[] =  "input/ListaPalavrasEN.txt";
	char encrypted_en[] = "output/ListaPalavrasENencrypted.txt";
	char decrypted_en[] = "output/ListaPalavrasENdecrypted.txt";

	print_bits(value);
	printf("Bits with value 0: %dx \n",count_zeros(value));
	printf("Bits with value 0: %dx \n",count_ones(value));
    printf("The most frequent symbol in %s :'%c'\n", pt_file, most_freq_symb(pt_file));
	printf("The most frequent symbol in %s :'%c'\n", en_file, most_freq_symb(en_file));

	negative_file(pt_file,encrypted_pt);
	negative_file(encrypted_pt,decrypted_pt);
	negative_file(en_file,encrypted_en);
	negative_file(encrypted_en,decrypted_en);

	return (0);
}