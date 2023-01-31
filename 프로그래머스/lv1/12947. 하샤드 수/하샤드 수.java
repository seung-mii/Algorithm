class Solution {
    public boolean solution(int x) {
        int digit = 0; int initx = x;
        
        while(x > 10) {
            digit += x % 10;
            x /= 10;
        }
        
        digit += x;
        return (initx % digit == 0) ? true : false;
    }
}