class Solution {
    public int solution(int left, int right) {
        int answer = 0; 
        
        for(int i = left; i <= right; i++) {
            int divisorNum = 0;
            for(int j = 1; j <= i; j++) {
                if(i % j == 0) divisorNum++;
            }
            
            // 약수의 개수가 짝수
            if(divisorNum % 2 == 0) answer += i;
            else answer -= i;
        }
        
        return answer;
    }
}