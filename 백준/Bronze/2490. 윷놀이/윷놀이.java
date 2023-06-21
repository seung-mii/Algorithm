import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        for(int i = 0; i < 3; i++) {
            int n = 0;
            for(int j = 0; j < 4; j++) {
                n += scanner.nextInt();
            }

            switch (n) {
                case 0:
                    System.out.println("D");
                    break;
                case 1:
                    System.out.println("C");
                    break;
                case 2:
                    System.out.println("B");
                    break;
                case 3:
                    System.out.println("A");
                    break;
                default:
                    System.out.println("E");
                    break;
            }
        }
    }
}