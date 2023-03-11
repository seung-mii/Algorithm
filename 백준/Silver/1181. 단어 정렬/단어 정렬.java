import java.io.*;
import java.util.Arrays;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        String ary1[][] = new String[N][2];

        for(int i = 0; i < N; i++) {
            ary1[i][0] = br.readLine();
            ary1[i][1] = String.valueOf(ary1[i][0].length());
        }

        // 람다식 & compare 사용
        Arrays.sort(ary1, (a1, a2) -> {
            if(Integer.parseInt(a1[1]) == Integer.parseInt(a2[1])) { // 길이가 같으면
                for(int i = 0; i < Integer.parseInt(a1[1]); i++) {
                    if((int)(a1[0].charAt(i)) != (int)(a2[0].charAt(i)))
                        return (int)(a1[0].charAt(i)) - (int)(a2[0].charAt(i));
                }
                return Integer.parseInt(a1[1]);
            }
            else
                return Integer.parseInt(a1[1]) - Integer.parseInt(a2[1]);
        });

        System.out.println(ary1[0][0]);
        for(int i = 1; i < N; i++) {
            if(!ary1[i][0].equals(ary1[i - 1][0])) // 중복 문자열 제거
                System.out.println(ary1[i][0]);
        }
        br.close();
    }
}