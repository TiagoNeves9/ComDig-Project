#include <stdio.h>

int count_ones(int val){

    int cnt = 0;
    while(val > 0){
        cnt += val & 1;
        val >>= 1;
    }
    return cnt;
};

int count_zeros(int val){
    int cnt = 0;
    while (val > 0)
    {
        cnt += (val & 1)^ 1;
        val >>= 1;
    }
    return cnt;
}

int main(){
    int x = count_ones(4);
    int z = count_zeros(4);
    printf("# of 1: %d, \n", x);
    printf("# of 0: %d, \n", z);

}