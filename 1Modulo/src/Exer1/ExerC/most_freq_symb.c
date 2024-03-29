#include <stdio.h>
#include <stdlib.h>
#include <string.h>


#define MAX_CH_SIZE ('~' - ' '+1)
#define FIRST_CH ' '

char most_freq_symb(char *file_name){


    int mostFreqCount = 0;
    int mostFreqChar = 0;
    FILE* ptr;
    int ch;
    char freq[MAX_CH_SIZE];

    ptr = fopen(file_name,"r");

    if (ptr == NULL)
    {
        printf("File can't be open");
        return '0';
    }

    for (ch = 0; ch < MAX_CH_SIZE; ch++)
    {
        freq[ch] = 0;
    }

    while (1)
    {
        ch = fgetc(ptr);
        if (ch == EOF) break;
        freq[ch-FIRST_CH]++;  
    }

    for (int i = 0; i < MAX_CH_SIZE; ++i)
    {
        if (freq[i] > mostFreqCount)
        {
            mostFreqCount = freq[i];
            mostFreqChar = i;

        }
    }

    printf("The most frequent character is '%c' with a number of %d occurrences", mostFreqChar + FIRST_CH, mostFreqCount);

    fclose(ptr);
    return mostFreqChar + ' ';    

}

void test_most_frequent_symbol()
{
    char *test_input_file = "test_input.txt";
    FILE *input_file = fopen(test_input_file, "w");
    fprintf(input_file, "File For Testing\nmost_frequent_symbol Function");
    fclose(input_file);
    input_file = fopen(test_input_file, "r");
    char actualSymbol = most_frequent_symb(input_file);
    char expectedSymbol = 'e';
    assert(actualSymbol == expectedSymbol);
    fclose(input_file);
}


int main(){

    most_freq_symb("text.txt");
    return 1;
}