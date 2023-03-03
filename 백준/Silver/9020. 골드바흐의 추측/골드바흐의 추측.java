import java.io.*;

public class Main {
    public static boolean[] prime = new boolean[10001];
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine());
        Prime();

        for(int i = 0; i<T; i++) {
            int n = Integer.parseInt(br.readLine()); //8
            int max = 0;

            for(int j = 2; j<n; j++) {
                if(prime[j] == false && prime[n-j] == false) {
                    if(max < n/2 && max < j)
                        max = j;
                }
            }
            System.out.println((n-max)+" "+max);
        }
    }

    public static void Prime() {
        prime[0] = prime[1] = true;
        for(int i = 2; i <= Math.sqrt(prime.length); i++) {
            if(prime[i])
                continue;
            for(int j = i * i; j < prime.length; j += i) {
                prime[j] = true;
            }
        }
    }
}