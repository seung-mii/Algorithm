import java.io.*;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int num = Integer.parseInt(br.readLine());
        int paper[][] = new int[100][100];
        int area = 0;

        for(int i = 0; i < num; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine(), " ");
            int X = Integer.parseInt(st.nextToken());
            int Y = Integer.parseInt(st.nextToken());
            for(int j = X; j < X + 10; j++) {
                for(int k = Y; k < Y + 10; k++) {
                    paper[j][k] = 1;
                }
            }
        }

        for(int j = 0; j < 100; j++) {
            for(int k = 0; k < 100; k++) {
                if(paper[j][k] == 1)
                    area++;
            }
        }

        System.out.println(area);
        br.close();
    }
}