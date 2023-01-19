import java.io.*;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        int body[][] = new int[N][2];
        int order = 1;

        for(int i = 0; i < N; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine(), " ");
            body[i][0] = Integer.parseInt(st.nextToken());  // x
            body[i][1] = Integer.parseInt(st.nextToken());  // y
        }

        for(int j = 0; j < N; j++) {
            for(int k = 0; k < N; k++) {
                if((body[j][0] < body[k][0]) && (body[j][1] < body[k][1])) 
                    // 본인보다 크면 등수++
                    order++;
            }
            
            System.out.print(order + " ");
            order = 1; // order 값 초기화
        }
    }
}
