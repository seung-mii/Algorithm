import java.util.*;

class Solution {
    public String solution(String s) {
        StringBuffer sb = new StringBuffer();
        int [] charNum = new int[s.length()];
        
        for(int i = 0; i < s.length(); i++) {
            charNum[i] = (int)(s.charAt(i));
        }
        
        Arrays.sort(charNum);
        
        for(int i = s.length() - 1; i > -1; i--) {
            sb.append((char)charNum[i]);
        }
        
        return sb.toString();
    }
}