import java.util.*;

class Solution {
    public int[] solution(int[] array, int[][] commands) {
        int[] answer = new int[commands.length];
        
        for(int n = 0; n < commands.length; n++) {
            int i = commands[n][0] - 1;
            int j = commands[n][1] - 1;
            int k = commands[n][2] - 1;
            int index = j - i + 1;
            int[] newArr = new int[index];
            
            for(int m = 0; m < index; m++) {
                newArr[m] = array[i++];
            }
            
            Arrays.sort(newArr);
            answer[n] = newArr[k];
        }
        
        return answer;
    }
}