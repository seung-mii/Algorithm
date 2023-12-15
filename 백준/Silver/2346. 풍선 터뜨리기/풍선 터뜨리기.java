import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        ArrayDeque<int[]> d = new ArrayDeque<>();
        int N = in.nextInt();

        for (int i = 0; i < N; i++) {
            int[] arr = {i + 1, in.nextInt()};
            d.offer(arr);
        }

        while (d.size() > 1) {
            int[] arr = d.poll();
            int n = arr[1];
            System.out.print(arr[0] + " ");

            if (n > 0) {
                for (int j = 1; j < n; j++) {
                    d.offerLast(d.pollFirst());
                }
            } else if (n < 0) {
                for (int j = n; j < 0; j++) {
                    d.offerFirst(d.pollLast());
                }
            }
        }

        System.out.print(d.poll()[0]);
    }
}