class Solution {
    boolean solution(String s) {
        int pNum = 0; int yNum = 0;

        for(int i = 0; i < s.length(); i++) {
            if(s.charAt(i) == 'p' || s.charAt(i) == 'P') pNum++;
            if(s.charAt(i) == 'y' || s.charAt(i) == 'Y') yNum++;
        }
        
        return pNum == yNum ? true : false;
    }
}