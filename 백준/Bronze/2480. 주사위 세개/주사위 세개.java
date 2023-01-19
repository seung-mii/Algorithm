import java.util.*;

public class Main { 
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int x = scanner.nextInt();
        int y = scanner.nextInt();
        int z = scanner.nextInt();
        
        if(x == y && y == z) // 세 개가 같은 눈
            System.out.print(10000+x*1000);
        else if((x == y && y != z) || (x == z && y != z)) 
            System.out.print(1000+x*100);
        else if (x != y && y == z)
            System.out.print(1000+y*100);
        else // 다 다른 눈
            System.out.print(Math.max(x, Math.max(y,z))*100);
    } 
}