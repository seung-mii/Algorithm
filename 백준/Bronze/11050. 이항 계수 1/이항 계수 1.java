import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner s = new Scanner(System.in);
        int N = s.nextInt();
        int K = s.nextInt();

        int answer = f(N)/(f(K)*f(N-K));
        System.out.print(answer);
    }

    private static int f(int n) {
        if(n > 2) n *= f(n-1);
        else if(n == 0) n = 1;
        return n;
    }
}