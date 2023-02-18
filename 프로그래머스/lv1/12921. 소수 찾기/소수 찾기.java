class Solution {
    public static boolean[] number;
    public int solution(int n) {
        int sum = 0;
        number = new boolean[n + 1];
        
        prime();
        for(int i = 2; i < n + 1; i++) {
            if(number[i] == false) sum++; // 소수라면 false
        }
        
        return sum;
    }
    
    public static void prime() { 
        number[0] = number[1] = true;
        
        for(int i = 2; i < Math.sqrt(number.length); i++) {
            if(number[i]) continue;
            for(int j = i * i; j < number.length; j += i) {
                number[j] = true;
            }
        }
    }
}