import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        long n = ((long)scanner.nextInt() - (long)scanner.nextInt());
        System.out.print(Math.abs(n));
    }
}