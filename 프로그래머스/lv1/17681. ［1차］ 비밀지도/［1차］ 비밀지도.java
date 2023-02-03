import java.util.*;

class Solution {
    public String[] solution(int n, int[] arr1, int[] arr2) {
        StringBuffer sb = new StringBuffer();
        String answer[] = new String[n];

        for(int i = 0; i < n; i++) {
            String s = "";
            String arr1Str = Integer.toString(arr1[i], 2);
            String arr2Str = Integer.toString(arr2[i], 2);
            
            for(int j = 0; j < n; j++) {
                if(arr1Str.length() < n) arr1Str = "0" + arr1Str;
                else if(arr2Str.length() < n) arr2Str = "0" + arr2Str;
            }

            for(int j = 0; j < n; j++) {
                if(arr1Str.charAt(j) == '0' && arr2Str.charAt(j) == '0') s += " ";
                else if(arr1Str.charAt(j) == '1') s += "#";
                else if(arr2Str.charAt(j) == '1') s += "#";
            }
            answer[i] = s;
        }
        return answer;
    }
}