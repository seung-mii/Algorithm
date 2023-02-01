class Solution {
    public boolean solution(String s) {
       int num = 0;
        
        for(int i = 0; i < s.length(); i++) {
            if((s.length() == 4 || s.length() == 6) && 
               ('0' <= s.charAt(i) && s.charAt(i) <= '9')) num++;
        }
        
        return num == s.length() ? true : false;
    }
}