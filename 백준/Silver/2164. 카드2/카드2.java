import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        Queue<Integer> q = new LinkedList<>();

        int N = in.nextInt();

        for (int i = 1; i < N + 1; i++) {
            q.offer(i);
        }

        while (q.size() != 1) {
            q.poll();

            int n = q.poll();
            q.offer(n);
        }
        
        System.out.println(q.peek());
    }
}