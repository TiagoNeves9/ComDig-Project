int count_ones(int val){

    int cnt = 0;
    while(val != 0){
        cnt = val & 1;
        val >>= 1;
    }
    return cnt;
};

int main(){
    int x = count_ones(44);
    printf("# of 1: %d, \n", x);
}
