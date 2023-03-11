import java.io.*;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        int coordinates[][] = new int[N][2];

        for(int i = 0; i < N; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine(), " ");
            coordinates[i][0] = Integer.parseInt(st.nextToken());
            coordinates[i][1] = Integer.parseInt(st.nextToken());
        }

        // 람다식 & compare 사용
        Arrays.sort(coordinates, (arr1, arr2) -> {
            if(arr1[0] == arr2[0])
                return Integer.compare(arr1[1], arr2[1]);
            else
                return Integer.compare(arr1[0], arr2[0]);
        });

        for(int i = 0; i < N; i++) {
            System.out.println(coordinates[i][0]+" "+coordinates[i][1]);
        }

        br.close();
    }
}