class Solution {
    public int solution(int[][] board) {
        int answer = 0;
        boolean landmine[][] = new boolean[board.length][board.length];
        
        for(int row = 0; row < landmine.length; row++) {
            for(int col = 0; col < landmine.length; col++) {
                if(board[row][col] == 1) Destroy(col, row, board.length, landmine);
            }
        }
        
        for(int i = 0; i < landmine.length; i++) {
            for(int j = 0; j < landmine.length; j++) {
                if(landmine[i][j] == false) answer++;
            }
        }
        
        return answer;
    }
    
    private static void Destroy(int col, int row, int n, boolean[][] landmine) {
        for(int r = row-1; r < row+2; r++) {
            if(r < 0 || r >= n) continue;
            else {
                for(int c = col-1; c < col+2; c++) {
                    if(c < 0 || c >= n) continue;
                    else landmine[r][c] = true;
                }
            }
        }
    }
    
}