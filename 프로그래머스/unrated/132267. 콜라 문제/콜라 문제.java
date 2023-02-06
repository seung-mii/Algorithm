class Solution {
    public int solution(int a, int b, int n) {
        int rest = n % a;
        int answer = (n / a) * b; 
        int have = answer + rest;
        
        while(a <= have) {
            rest = have % a;
            answer += (have / a) * b; 
            have = ((have / a) * b + rest);
        }
        
        return answer;
    }
}