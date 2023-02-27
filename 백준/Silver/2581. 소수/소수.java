import java.io.*;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int M = Integer.parseInt(br.readLine());
        int N = Integer.parseInt(br.readLine());
        int sum = 0; int min = 10000;

        for(int i = M; i < N+1; i++) { //61
            boolean temp = false;
            for(int j = 2; j < i; j++) {
                if(i % j == 0)
                    temp = true;
            }

            if(temp == false && i != 1) {
                sum += i;
                if(min > i)
                    min = i;
            }
        }

        if(sum == 0)
            System.out.println("-1");
        else {
            System.out.println(sum);
            System.out.println(min);
        }
    }
}