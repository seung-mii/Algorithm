import java.util.*;

class Solution {
    public int solution(int n) {
        StringBuffer sb = new StringBuffer();
        
        // 10진법 -> 3진법
        String three = Integer.toString(n, 3);
        
        // 앞 뒤 반전
        for(int i = three.length() - 1; i > -1; i--) {
            sb.append(three.charAt(i));
        }
        
        // 3진법 -> 10진법
        int ten = Integer.parseInt(sb.toString(), 3);
        return ten;
    }
}