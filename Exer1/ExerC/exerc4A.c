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


void_test(void){

    TEST_ASSERT_EQUAL(2,count_ones(4));
    TEST_ASSERT_EQUAL(2,count_zeros(4));

    
}


int main(){
    

}