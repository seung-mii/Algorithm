class Solution {
    public String solution(String s, int n) {
        StringBuffer sb = new StringBuffer();
        
        for(int i = 0; i < s.length(); i++) {
            int nextChar = (int)(s.charAt(i) + n);
            if('A' <= s.charAt(i) && s.charAt(i) <= 'Z') {
                if(nextChar > 90) nextChar -= 26;
                sb.append((char)nextChar);
            }
            else if('a' <= s.charAt(i) && s.charAt(i) <= 'z') {
                if(nextChar > 122) nextChar -= 26;
                sb.append((char)nextChar);
            }
            else if (s.charAt(i) == ' ') sb.append(' ');
        }
        
        return sb.toString();
    }
}