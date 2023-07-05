import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        StringBuilder sb = new StringBuilder();
        int N = in.nextInt();
        int[] arr = new int[N];

        for(int i = 0; i < N; i++) {
            arr[i] = in.nextInt();
        }

        Arrays.sort(arr);

        int M = in.nextInt();

        for(int i = 0; i < M; i++) {
            if(binary(arr, in.nextInt()) >= 0) sb.append(1).append('\n');
            else sb.append(0).append('\n');
        }
        System.out.println(sb);
    }

    public static int binary(int[] arr, int key) {
        int lo = 0;
        int hi = arr.length - 1;

        while(lo <= hi) {
            int mid = (lo + hi) / 2;

            if(key < arr[mid]) hi = mid - 1;
            else if(key > arr[mid]) lo = mid + 1;
            else return mid;
        }

        return -1;
    }
}