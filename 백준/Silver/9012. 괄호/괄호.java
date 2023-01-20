import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        StringBuilder sb = new StringBuilder();

        for(int i = 0; i < N; i++) {
            int left = 0;
            String str = br.readLine();
            for(int j = 0; j < str.length(); j++) {
                if(str.charAt(j) == 40) left++;
                else left--;

                if(left < 0) {
                    sb.append("NO").append('\n');
                    break;
                }
            }
            if(left == 0) sb.append("YES").append('\n');
            else if(left > 0) sb.append("NO").append('\n');
        }
        System.out.println(sb);
    }
}