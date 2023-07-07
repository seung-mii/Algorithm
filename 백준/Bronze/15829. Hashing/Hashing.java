import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner s = new Scanner(System.in);
        int answer = 0;
        int L = s.nextInt();
        String str = s.next();

        for (int i = 0; i < L; i++) {
            answer += (int)((str.charAt(i) - 96) * (Math.pow(31, i)));
        }

        System.out.println(answer);
    }
}