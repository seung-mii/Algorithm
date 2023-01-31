class Solution {
    public long solution(int a, int b) {
        long sum = 0;
        
        while(a != b) {
            if(a < b) {
                sum += a;
                a++;
            } else {
                sum += b;
                b++;
            }
        }
        
        sum += a;
        return sum;
    }
}