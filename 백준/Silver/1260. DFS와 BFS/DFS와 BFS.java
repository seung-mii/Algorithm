import java.util.*;

public class Main {
    static int N;
    static int M;
    static int V;
    static int check[][];
    static boolean checked[];

    public static void main(String[] args) {
        Scanner s = new Scanner(System.in);
        N = s.nextInt();
        M = s.nextInt();
        V = s.nextInt();
        check = new int[N+1][N+1];
        checked = new boolean[N+1];

        for(int i = 0; i < M; i++) {
            int a = s.nextInt();
            int b = s.nextInt();
            check[a][b] = check[b][a] = 1;
        }

        dfs(V);
        checked = new boolean[N+1];
        System.out.println();

        bfs();
    }

    public static void dfs(int i) {
        checked[i] = true;
        System.out.print(i + " ");

        for(int j = 1; j <= N; j++) {
            if(check[i][j] == 1 && checked[j] == false) {
                dfs(j);
            }
        }
    }

    public static void bfs() {
        Queue<Integer> queue = new LinkedList<Integer>();
        queue.offer(V);
        checked[V] = true;
        System.out.print(V + " ");

        while(!queue.isEmpty()) {
            int temp = queue.poll();

            for(int j = 1; j <= N; j++) {
                if(check[temp][j] == 1 && checked[j] == false) {
                    queue.offer(j);
                    checked[j] = true;
                    System.out.print(j + " ");
                }
            }
        }
    }
}