class Solution {
    public int solution(int[][] dots) {
        int answer = 0; int index = 0;
        double slope[] = new double[6];
        
        for(int i = 0; i < 4; i++) {
            for(int j = i; j < 3; j++) {
                slope[index] = (((double)dots[i][1] - (double)dots[j+1][1]) / 
                               ((double)dots[i][0] - (double)dots[j+1][0]));
                double temp = slope[index];
                index++; 

                for(int k = 0; k < index - 1; k++) {
                    if(temp == slope[k]) {
                        answer = 1;
                        break;
                    }
                }
            }
        }
        
        return answer;
    }
}