import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String s[] = scanner.next().split("");
        String english[] = {"a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"};
        int ary[] = new int[26];

        for (int i = 0; i < s.length; i++) {
            for (int j = 0; j < english.length; j++) {
                if(s[i].equals(english[j])) ary[j]++;
            }
        }

        for(int i = 0; i < ary.length; i++) {
            System.out.print(ary[i] + " ");
        }
    }
}