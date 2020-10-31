// Reverse the bits of an 32 bit unsigned integer A.
// 0 <= A <= 232

unsigned int Solution::reverse(unsigned int A) {
    unsigned int ans;
    int i;
    ans=0;
    for(i=0;i<32;i++){
        if(A &(1<<i)){
            ans |= 1 <<(32-i-1);
        }
    }
    return ans;
}