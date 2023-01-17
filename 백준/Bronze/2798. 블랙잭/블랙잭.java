import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine(), " ");

        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());
        int[] arr = new int[N];
        int result = 0;

        st = new StringTokenizer(br.readLine(), " ");
        for (int i = 0; i < N; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
        }

        for (int l = 0; l < N-2; l++) {
            if (arr[l] > M) // 하나의 카드가 M보다 클 경우
                continue;

            for (int j = l+1; j < N-1; j++) {
                if (arr[l] + arr[j] > M) // 두 개의 카드의 합이 M보다 클 경우
                    continue;

                for (int k = j+1; k < N; k++) {
                    int temp = arr[l] + arr[j] + arr[k];

                    if (M == temp) { // M과 세 카드의 합이 같은 경우
                        result = temp;
                        break;
                    }

                    if (result < temp && temp < M) // 세 카드의 합이 이전 합보다 크면서 M보다 작을 경우
                        result = temp;
                }
            }
        }
        
        System.out.println(result);
    }
}