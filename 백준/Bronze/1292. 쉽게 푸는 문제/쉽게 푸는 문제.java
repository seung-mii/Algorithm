import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner s = new Scanner(System.in);
        int num[] = new int[10000];

        int x = 0;
        for(int i = 1; i < 50; i++) {
            for(int j = i; j < i + i; j++) {
                num[x++] = i;
            }
        }

        int answer = 0;
        int start = s.nextInt(); int end = s.nextInt();
        for(int i = start - 1; i < end; i++){
            answer += num[i];
        }

        System.out.println(answer);
    }
};