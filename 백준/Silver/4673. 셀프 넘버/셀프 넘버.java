import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) {
        self();
    }

    public static void self() {
        boolean []N = new boolean[10000];
        for(int i = 1; i<10000; i++) {
            N[i] = true; // 모두 true
        }

        int num = 0;
        for(int i = 1; i<10000; i++) {
            if(i < 10)
                num = i+i;
            else if (9 < i && i < 100)
                num = i + (i/10) + (i%10);
            else if (99 < i && i < 1000)
                num = i + (i/100) + ((i%100)/10) + (i%10);
            else
                num = i + (i/1000) + ((i%1000)/100) + ((i%100)/10) + (i%10);

            if(num < 10000)
                N[num] = false;
        }

        for(int i = 1; i<10000; i++) {
            if(N[i] == true)
                System.out.println(i);
        }
    }
}
