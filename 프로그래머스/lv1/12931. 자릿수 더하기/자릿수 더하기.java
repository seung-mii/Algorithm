import java.util.*;

public class Solution {
    public int solution(int n) {
        int answer = 0;
        String nString = String.valueOf(n);
        
        for(int i = 0; i < nString.length(); i++) {
            answer += Integer.parseInt(String.valueOf(nString.charAt(i)));
        }
        
        return answer;
    }
}