import java.util.*;

public class Main {

    public static void main(String[] args) {
        // TODO Auto-generated method stub
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] arr = new int[n];
        int[] freq = new int[8001]; // 정수의 절댓값은 4000이 넘지 않기 때문에
        int sum = 0; int second = 0; // 두 번쨰로 작은 값 저장 변수
        int count = 0; int max = 0;

        for (int i = 0; i < n; i++) {
            arr[i] = sc.nextInt();
            sum += arr[i];
        }

        Arrays.sort(arr); // 배열 정렬

        // 최빈값 구하기
        for (int i = 0; i < n; i++) {
            freq[arr[i] + 4000]++;
            max = Math.max(max, freq[arr[i] + 4000]);
        }

        for (int i = 0; i < freq.length; i++) {
            if (freq[i] == max) {
                count++;
                second = i - 4000;
            }

            if (count == 2) { // 최빈값이 두 개 이상일 경우 두 번째로 작은 값을 찾아 저장
                second = i - 4000;
                break;
            }
        }

        System.out.println((int)Math.round((double) sum / (double) n)); // 합
        System.out.println(arr[(arr.length/2)]); // 중앙값
        System.out.println(second);
        System.out.println(arr[n-1]-arr[0]); // 범위
    }
}