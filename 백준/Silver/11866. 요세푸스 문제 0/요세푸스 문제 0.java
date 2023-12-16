import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        Queue<Integer> q = new LinkedList<>();
        int N = in.nextInt();
        int K = in.nextInt();

        for (int i = 1; i < N + 1; i++) {
            q.offer(i);
        }

        System.out.print("<");
        while (q.size() != 1) {
            for (int i = 0; i < K - 1; i++) {
                q.offer(q.poll());
            }
            System.out.print(q.poll() + ", ");
        }
        System.out.print(q.peek() + ">");
    }
}