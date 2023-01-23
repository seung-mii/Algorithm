class Solution {
    public int solution(int[] common) {
        int answer = 0;
        boolean flag = false; // 등비수열 = true
        
        if((common[1] - common[0]) == (common[2] - common[1])) // 등차수열일 경우
            flag = true;
        
        if(flag == true) {
            int allowance = common[1] - common[0];
            answer = common[common.length-1] + allowance;
        } else {
            int arithmetic = common[1] / common[0];
            answer = common[common.length-1] * arithmetic;
        }
        
        return answer;
    }
}