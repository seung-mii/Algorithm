import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner s = new Scanner(System.in);
        int n = s.nextInt();

        for(int i = 0; i < n; i++) {
            int a = s.nextInt();
            int b = s.nextInt();
            int r = a % 10;

            for (int j = 1; j < b; j++) {
                r = (r * a) % 10;
            }
            if(r == 0) r = 10;

            System.out.println(r);
        }
    }
}