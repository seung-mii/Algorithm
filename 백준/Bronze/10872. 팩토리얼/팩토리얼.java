import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        int result = factorial(N);
        System.out.print(result);
    }
    public static int factorial(int n) {
        if(n < 2)
            return 1;
        return n*factorial(n-1);
    }
}
