import java.util.*;

class Solution {
    public static void op(StringBuffer sb, int[] food, int i) {
        int repeat = food[i]/2;

        for(int j = 0; j < repeat; j++) {
            sb.append(i);
        }
    }
    
    public String solution(int[] food) {
        StringBuffer sb = new StringBuffer();
        int i = 0; 
        
        while(i != (food.length - 1)) {
            i++;
            op(sb, food, i);
        }
        
        sb.append(0);
        
        while(i != 0) {
            op(sb, food, i);
            i--;
        }
        
        return sb.toString();
    }
}