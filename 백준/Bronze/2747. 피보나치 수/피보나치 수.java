import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner s = new Scanner(System.in);
        int n = s.nextInt();
        int f1 = 0; int f2 = 1;
        int answer = f1 + f2;

        for(int i = 2; i < n; i++) {
            f1 = f2;
            f2 = answer;
            answer = f1 + f2;
        }

        System.out.print(answer);
    }
};