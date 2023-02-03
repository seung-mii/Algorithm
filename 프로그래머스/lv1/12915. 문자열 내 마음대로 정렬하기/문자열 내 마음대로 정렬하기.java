import java.util.*;

class Solution {
    public String[] solution(String[] strings, int n) {
        Arrays.sort(strings);
        
        Arrays.sort(strings, new Comparator<String>() {
            public int compare(String s1, String s2) {
                return s1.charAt(n) - s2.charAt(n);
            }
        });
        
        return strings;
    }
}