import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner s = new Scanner(System.in);
        int num[] = new int[s.nextInt()];

        int index = 0;
        for(int i = 0; i < num.length; i++) {
            int input = s.nextInt();
            
            if(index > 0 && input == 0) num[--index] = 0;
            else {
                num[index] = input;
                index++;
            }
        }

        int answer = 0;
        for(int i = 0; i < num.length; i++) {
            answer += num[i];
        }

        System.out.print(answer);
    }
};