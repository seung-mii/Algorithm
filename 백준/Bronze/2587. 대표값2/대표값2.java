import java.io.*;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int num[] = new int[5];
        int sum = 0;

        for(int i = 0; i < 5; i++) {
            num[i] = Integer.parseInt(br.readLine());
            sum += num[i];
        }

        Arrays.sort(num);
        System.out.println(sum / 5);
        System.out.println(num[2]);
        br.close();
    }
}