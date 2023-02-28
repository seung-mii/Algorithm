import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int repeat = Integer.parseInt(br.readLine());
        double []result = new double[repeat];

        for(int i = 0; i<repeat; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine(), " ");
            int index = Integer.parseInt(st.nextToken());
            int []score = new int[index];
            int num = 0; // 평균 넘는 학생 수
            int sum = 0; // 점수 총 합

            for(int j = 0; j<index; j++) {
                score[j] = Integer.parseInt(st.nextToken());
                sum += score[j];
            }

            double avg = (double) (sum/index);
            for(int j = 0; j<index; j++) {
                if (score[j] > avg)
                    num++;
            }
            result[i] = (double) num/index;
        }

        for(int i = 0; i<repeat; i++) {
            System.out.printf("%.3f%%\n", result[i]*100);
        }

        br.close();
    }
}
