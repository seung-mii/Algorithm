import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner s = new Scanner(System.in);
        int T = s.nextInt();
        int Acount = 0; int Bcount = 0; int Ccount = 0;

        if(T % 10 == 0) {
            if (T >= 300) {
                Acount += T / 300;
                T %= 300;
            }
            if (T >= 60) {
                Bcount += T / 60;
                T %= 60;
            }
            if (T >= 10) {
                Ccount += T / 10;
                T %= 10;
            }
            System.out.print(Acount + " " + Bcount + " " + Ccount);
        } else System.out.print(-1);
    }
}