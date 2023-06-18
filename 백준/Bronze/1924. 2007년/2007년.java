import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner s = new Scanner(System.in);
        int x = s.nextInt();
        int y = s.nextInt();

        String week[] = {"SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"};
        int day[] = { 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31 };
        int num = 0;

        for(int i = 1; i < x; i++) {
            num += day[i - 1];
        }
        num += y;

        System.out.print(week[num % 7]);
    }
};