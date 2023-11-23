import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner s = new Scanner(System.in);
        int ary[] = new int[6];
        int x = 0; int y = 0;

        for (int i = 0; i < 6; i++) {
            ary[i] = s.nextInt();
        }

        for (x = -999; x < 1000; x++) {
            for (y = -999; y < 1000; y++) {
                if (ary[0] * x + ary[1] * y == ary[2] && ary[3] * x + ary[4] * y == ary[5]) {
                    System.out.println(x + " " + y);
                }
            }
        }
    }
}
