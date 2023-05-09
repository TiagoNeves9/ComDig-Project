#include <stdio.h>

void print_bits(int val) {
    int i;
    for (i = sizeof(int) * 8 - 1; i >= 0; i--) {    //sizeof retorna o valor de int em bytes, 
                                                    //*8 converte para bits, 
                                                    //-1 obtemos o indice mais significativo
        putchar((val & (1 << i)) ? '1' : '0');
    }
    putchar('\n');
}

int main(){
    printf("::     Starting Tests     :::\n");
    printf("::     Testing with 0     :::\n");
    print_bits(0);
    printf("\n");
    printf("::     Testing with 1     :::\n");
    print_bits(1);
    printf("\n");
    printf("::     Testing with 2     :::\n");
    print_bits(2);
    printf("\n");
    printf("::     Testing with 10     :::\n");
    print_bits(10);
    printf("\n");
    printf("::     Testing with 255     :::\n");
    print_bits(255);
    printf("\n");
}