import java.io.*;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        int count = 0;
        StringTokenizer st = new StringTokenizer(br.readLine(), " ");

        for(int i = 0; i < N; i++) {
            int num = Integer.parseInt(st.nextToken());
            boolean temp = false;
            for(int j = 2; j < num; j++) {
                if(num % j == 0)
                    temp = true;
            }
            if(temp == false && num != 1)
                count++;
        }
        System.out.print(count);
    }
}