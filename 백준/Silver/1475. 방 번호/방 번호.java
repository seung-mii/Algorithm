import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String s[] = scanner.next().split("");
        String num[] = { "0", "1", "2", "3", "4", "5", "6", "7", "8" };
        int count[] = new int[9]; int set = 1;

        for(int i = 0; i < s.length; i++) {
            for (int j = 0; j < num.length; j++) {
                if (s[i].equals("9")) {
                    count[6]++;
                    break;
                } else if (s[i].equals(num[j])) {
                    count[j]++;
                    break;
                }
            }
        }

        for(int j = 0; j < num.length; j++) {
            int six = (int)Math.round((double)count[6]/2);

            if(j != 6 && set < count[j]) set = count[j];
            else if(j == 6 && set < six) set = six;
        }

        System.out.print(set);
    }
}