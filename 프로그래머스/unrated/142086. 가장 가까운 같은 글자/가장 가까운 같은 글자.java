class Solution {
    public int[] solution(String s) {
        int[] result = new int[s.length()];
        
        for(int i = 0; i < s.length(); i++) {
            for(int j = 0; j < i; j++) {
                if(s.charAt(i) == s.charAt(j)) result[i] = i - j;
            }
            if(result[i] == 0) result[i] = -1;
        }
        
        return result;
    }
}