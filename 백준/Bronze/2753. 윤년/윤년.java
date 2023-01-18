import java.util.*;

public class Main { 
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int score = scanner.nextInt();
        
        if(score % 4 == 0 && score % 100 != 0 || score % 400 == 0)
            // 나눴을 때 나머지가 없다면 = 배수라면 
            System.out.print("1");
        else 
            System.out.print("0");
    } 
}