#include <stdio.h>

void print_bits(int val) {
    int i;
    for (i = sizeof(int) * 8 - 1; i >= 0; i--) {
        putchar((val & (1 << i)) ? '1' : '0');
    }
    putchar('\n');
}

int main(){
    print_bits(2);
    print_bits(7);
    return 0;
}