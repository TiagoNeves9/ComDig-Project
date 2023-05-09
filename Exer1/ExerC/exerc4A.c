#include <stdio.h>
#include <unity.h>

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


void test_count_ones()
{
    assert(count_ones(0) == 0);
    assert(count_ones(1) == 1);
    assert(count_ones(2) == 1);
    assert(count_ones(3) == 2);
    assert(count_ones(4) == 1);
    assert(count_ones(5) == 2);
    assert(count_ones(6) == 2);
    assert(count_ones(7) == 3);
    assert(count_ones(8) == 1);
}

void test_count_zeros()
{
    assert(count_zeros(0) == 1);
    assert(count_zeros(1) == 0);
    assert(count_zeros(2) == 1);
    assert(count_zeros(3) == 0);
    assert(count_zeros(4) == 2);
    assert(count_zeros(5) == 1);
    assert(count_zeros(6) == 1);
    assert(count_zeros(7) == 0);
    assert(count_zeros(8) == 3);
}


int main(){
    

}