class Solution {
    public int solution(String A, String B) {
        int result = 0;
        StringBuffer sb = new StringBuffer(A); // Hello -> oHell
        String test = sb.toString();
        
        for(int j = 0; j < A.length() - 1; j++) {
            if((test.toString()).equals(B)) break;
            
            test = test.substring(A.length() - 1, A.length()) + test.substring(0, A.length() - 1);
            result++;
            
            if(!(test.toString()).equals(B) && j == A.length() - 2) result = -1;
        }
        
        return result;
    }
}