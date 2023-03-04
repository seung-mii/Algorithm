import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        int N = Integer.parseInt(br.readLine());
        int num[] = new int[10001];

        for(int i = 0; i < N; i++) {
            num[Integer.parseInt(br.readLine())]++;
        }

        for(int i = 1; i < 10001; i++) {
            while (num[i] > 0) {
                sb.append(i).append("\n");
                num[i]--;
            }
        }

        System.out.println(sb);
        br.close();
    }
}