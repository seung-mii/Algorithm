import java.util.*;

class Solution {
    public int[] solution(int[] answers) {
        int[] one = { 1, 2, 3, 4, 5 };
        int[] two = { 2, 1, 2, 3, 2, 4, 2, 5 };
        int[] three = { 3, 3, 1, 1, 2, 2, 4, 4, 5, 5 };
        int oneScore = 0; int twoScore = 0; int threeScore = 0;
        Queue<Integer> q = new LinkedList<>();
        
        for(int i = 0; i < answers.length; i++) {
            if(answers[i] == one[i % 5]) oneScore++;
            if(answers[i] == two[i % 8]) twoScore++;
            if(answers[i] == three[i % 10]) threeScore++;
        }
        
        int maxScore = Math.max(Math.max(oneScore, twoScore), threeScore);
        if(maxScore == oneScore) q.add(1);
        if(maxScore == twoScore) q.add(2);
        if(maxScore == threeScore) q.add(3);
        
        return q.stream().mapToInt(Integer::intValue).toArray();
    }
}