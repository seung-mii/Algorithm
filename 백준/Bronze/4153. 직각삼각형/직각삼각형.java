import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner s = new Scanner(System.in);

        while(true) {
            int ary[] = new int[3];
            ary[0] = s.nextInt();
            ary[1] = s.nextInt();
            ary[2] = s.nextInt();
            
            Arrays.sort(ary);

            if(ary[0] == 0) break;
            if(Math.pow(ary[2], 2) == Math.pow(ary[0], 2) + Math.pow(ary[1], 2))
                System.out.println("right");
            else
                System.out.println("wrong");
        }
    }
}