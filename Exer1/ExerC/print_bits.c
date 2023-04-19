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
    print_bits(2);
    print_bits(7);
    print_bits(-1);
    print_bits(32);
    return 0;
}