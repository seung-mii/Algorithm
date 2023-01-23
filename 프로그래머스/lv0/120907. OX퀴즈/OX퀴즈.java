import java.util.StringTokenizer;

class Solution {
    public String[] solution(String[] quiz) {
        String[] answer = new String[quiz.length];
        
        for(int i = 0; i < quiz.length; i++) {
            StringTokenizer st = new StringTokenizer(quiz[i], " ");
            int X = Integer.parseInt(st.nextToken());
            String operator = st.nextToken();
            int Y = Integer.parseInt(st.nextToken()); 
            st.nextToken(); // 버리는 값
            int Z = Integer.parseInt(st.nextToken());
            
            if(operator.equals("-")) answer[i] = (X - Y == Z ? "O" : "X");
            else answer[i] = (X + Y == Z ? "O" : "X");
        }
        
        return answer;
    }
}