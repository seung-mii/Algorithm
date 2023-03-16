import java.io.*;

public class Main {
    public static boolean[] prime;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        while(true) {
            int n = Integer.parseInt(br.readLine());
            if(n == 0)
                break;

            int count = 0;
            prime = new boolean[2*n + 1];
            get_prime();

            for(int i = n+1; i <= (2*n); i++) {
                if(prime[i] == false)
                    count++;
            }

            System.out.println(count);
        }
    }
    
    public static void get_prime() {
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