import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner s = new Scanner(System.in);
        int N = s.nextInt();
        int[] ary = new int[N];

        for(int i = 0; i < N; i++) {
            ary[i] = s.nextInt();
        }

        Arrays.sort(ary);

        int M = s.nextInt();
        StringBuilder sb = new StringBuilder();

        for(int i = 0; i < M; i++) {
            int num = s.nextInt();
            sb.append(upperBound(ary, num) - lowerBound(ary, num)).append(' ');
        }
        System.out.println(sb);
    }

    private static int lowerBound(int[] ary, int num) {
        int start = 0;
        int end = ary.length;

        while (start < end) {
            int mid = (start + end) / 2;

            if (num <= ary[mid]) end = mid;
            else start = mid + 1;
        }
        return start;
    }

    private static int upperBound(int[] ary, int num) {
        int start = 0;
        int end = ary.length;

        while (start < end) {
            int mid = (start + end) / 2;

            if (num < ary[mid]) end = mid;
            else start = mid + 1;
        }
        return start;
    }
}