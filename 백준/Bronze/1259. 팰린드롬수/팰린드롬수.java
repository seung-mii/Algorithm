import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String n = scanner.next();

        while(!n.equals("0")) {
            String s[] = n.split("");
            String arr[] = new String[(int)s.length / 2];
            int len = arr.length;

            if(s.length == 1) System.out.println("yes");

            for(int i = 0; i < len; i++) {
                arr[i] = s[i];
            }

            if(s.length % 2 == 0) repeat(arr, s, len);
            else { // 홀수
                len++;
                repeat(arr, s, len);
            }

            n = scanner.next();
        }
    }

    private static void repeat(String[] arr, String[] s, int len) {
        for(int i = arr.length - 1; i > -1; i--) {
            if(!arr[i].equals(s[len++])) {
                System.out.println("no");
                break;
            } else if(i == 0) System.out.println("yes");
        }
    }
};