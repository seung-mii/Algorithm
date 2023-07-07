import java.util.*;

public class Main {
    public static boolean[][] arr;
    public static int min = 64;

    public static void main(String[] args) {
        Scanner s = new Scanner(System.in);
        int N = s.nextInt();
        int M = s.nextInt();
        
        arr = new boolean[N][M];
        for (int i = 0; i < N; i++) {
            String str = s.next();

            for (int j = 0; j < M; j++) {
                if (str.charAt(j) == 'W') arr[i][j] = true;
                else arr[i][j] = false;
            }
        }

        int row_start = N - 7;
        int col_start = M - 7;

        for (int i = 0; i < row_start; i++) {
            for (int j = 0; j < col_start; j++) {
                find(i, j);
            }
        }
        System.out.println(min);
    }
    
    public static void find(int x, int y) {
        int x_end = x + 8;
        int y_end = y + 8;
        int count = 0;

        boolean TF = arr[x][y];

        for (int i = x; i < x_end; i++) {
            for (int j = y; j < y_end; j++) {
                if (arr[i][j] != TF) count++;
                TF = !TF;
            }
            TF = !TF;
        }

        count = Math.min(count, 64 - count);
        min = Math.min(min, count);
    }
}