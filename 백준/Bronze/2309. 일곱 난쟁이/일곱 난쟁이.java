import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner s = new Scanner(System.in);
        int arr[] = new int[9]; int sum = 0;

        for(int i = 0; i < 9; i++) {
            arr[i] = s.nextInt();
            sum += arr[i];
        }

        for(int i = 0; i < 8; i++) {
            for(int j = i + 1; j < 9; j++) {
                if((sum - arr[i] - arr[j]) == 100) {
                    arr[i] = 0; arr[j] = 0;
                    break;
                }
            }
            if(arr[i] == 0) break;
        }

        Arrays.sort(arr);

        for(int i = 2; i < 9; i++) {
            System.out.println(arr[i]+ " ");
        }
    }
}