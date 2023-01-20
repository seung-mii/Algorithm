import java.io.*;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());

        for(int i = 0; i < N; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine(), " ");
            int tokenNum = st.countTokens();
            // 밑에 st.nextToken()을 쓰면서 남은 토큰의 개수가 자꾸 바뀌기 때문에
            // 첫 토큰의 개수를 남기려고 변수 설정
            for(int j = 0; j < tokenNum; j++) {
                // 토큰 하나씩 뒤집은 걸 출력
                StringBuilder sb = new StringBuilder(st.nextToken());
                System.out.print(sb.reverse() + " ");
            }
        }
    }
}