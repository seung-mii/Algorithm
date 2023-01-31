import java.util.*;

class Solution {
    public long solution(long n) {
        StringBuffer sb = new StringBuffer();
        int temp[] = new int[String.valueOf(n).length()];
        
        for(int i = 0; i < String.valueOf(n).length(); i++) {
            temp[i] = (String.valueOf(n)).charAt(i) - '0';
        }
        
        Arrays.sort(temp);
        
         for(int j = temp.length - 1; j > -1; j--) {
            sb.append(temp[j]);
        }
        
        return Long.parseLong(sb.toString());
    }
}