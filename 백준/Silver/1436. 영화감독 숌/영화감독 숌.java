import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());

        int num = 666;
        int count = 1;

        while(count != N) { // count가 N번째의 N의 값과 동일해지면 종료
            num++;
            if(String.valueOf(num).contains("666")) // 문자열에 666이 포함되어 있다면
                count++;
        }

        System.out.println(num);
    }
}