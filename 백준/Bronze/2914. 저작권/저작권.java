import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner s = new Scanner(System.in);
        int song = s.nextInt() * (s.nextInt() - 1) + 1;
        System.out.print(song);
    }
}