import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner s = new Scanner(System.in);
        int n = s.nextInt();

        for(int i = 0; i < n; i++) {
            int arr[] = new int[10];

            for(int j = 0; j < 10; j++) {
                arr[j] = s.nextInt();
            }

            Arrays.sort(arr);
            System.out.println(arr[7]);
        }
    }
}