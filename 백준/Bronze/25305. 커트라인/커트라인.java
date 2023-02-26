import java.io.*;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine(), " ");
        int N = Integer.parseInt(st.nextToken());  // 응시자
        int k = Integer.parseInt(st.nextToken());  // 상을 받는 사람의 수
        int score[] = new int[N];

        StringTokenizer st2 = new StringTokenizer(br.readLine(), " ");
        for(int i = 0; i < N; i++) {
            score[i] = Integer.parseInt(st2.nextToken());
        }

        Arrays.sort(score);
        System.out.println(score[N-k]);
        br.close();
    }
}