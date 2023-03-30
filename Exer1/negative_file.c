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

int main(){

    negative_file("text.txt", "result.txt");
    return 1;
}