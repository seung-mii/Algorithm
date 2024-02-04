import java.util.*;

public class Main {
    public static int[] arr;
    public static boolean[] visit;

    public static void dfs(int n, int m, int depth) {
        if (depth == m) {
            for (int index : arr) {
                System.out.print(index + " ");
            }
            System.out.println();
            return;
        }

        for (int i = 0; i < n; i++) {
            if (visit[i] == false) {
                visit[i] = true;
                arr[depth] = i + 1;
                dfs(n, m, depth + 1);

                visit[i] = false;
            }
        }

    }

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int N = in.nextInt();
        int M = in.nextInt();

        arr = new int[M];
        visit = new boolean[N];
        dfs(N, M, 0);
    }
}
