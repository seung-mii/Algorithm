class Solution {
    public int[] solution(long n) {
        String nString = String.valueOf(n);
        int[] answer = new int[nString.length()];
        
        for(int i = 0; i < nString.length(); i++) {
            answer[i] = Integer.parseInt(String.valueOf(nString.charAt(nString.length() - i - 1)));
        }
        
        return answer;
    }
}