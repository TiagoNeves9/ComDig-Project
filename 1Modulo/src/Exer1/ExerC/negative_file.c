#include <stdio.h>
#include <stdlib.h>
#include <string.h>


void negative_file(char *input_file_name, char *output_file_name){

FILE* inp, *outp;
int ch;

inp = fopen(input_file_name, "rb");
outp = fopen(output_file_name, "wb");

while (1)
    {   
        ch = fgetc(inp);
        if (ch == EOF) break;
        fputc(~ch,outp);
    }

fclose(outp);
fclose(inp);    

}

void test_negative_file()
{
    char *test_input_file = "test_input.txt";
    char *test_output_file = "test_output.txt";
    char *expected_output_file = "test_negative_expected.txt";
    FILE *input_file = fopen(test_input_file, "w");
    fprintf(input_file, "File For Testing\nnegative_file Function");
    fclose(input_file);
    negative_file(test_input_file, test_output_file);
    FILE *output_file = fopen(test_output_file, "r");
    FILE *expected_file = fopen(expected_output_file, "r");
    int output_char = fgetc(output_file);
    int expected_char = fgetc(expected_file);
    while (output_char != EOF && expected_char != EOF)
    {
        assert(output_char == expected_char);
        output_char = fgetc(output_file);
        expected_char = fgetc(expected_file);
    }
    assert(output_char == EOF && expected_char == EOF);
    fclose(output_file);
    fclose(expected_file);
    remove(test_input_file);
    remove(test_output_file);
}

int main(){

    negative_file("text.txt", "result.txt");
    return 1;
}