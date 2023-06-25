import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner s = new Scanner(System.in);
        int max = 0;
        int pre = s.nextInt() + s.nextInt();

        for(int i = 0; i < 9; i++) {
            if(max < pre) max = pre;
            pre = pre - s.nextInt() + s.nextInt();
        }
        System.out.print(max);
    }
}