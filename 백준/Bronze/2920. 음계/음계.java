import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner s = new Scanner(System.in);
        int as[] = { 1, 2, 3, 4, 5, 6, 7, 8 };
        int de[] = { 8, 7, 6, 5, 4, 3, 2, 1 };
        int a = 0; int d = 0;

        for(int i = 0; i < 8; i++) {
            int num = s.nextInt();
            if (as[i] == num) a++;
            else if (de[i] == num) d++;
        }

        if (a == 8) System.out.println("ascending");
        else if (d == 8) System.out.println("descending");
        else System.out.println("mixed");
    }
};