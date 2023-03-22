import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int num = Integer.parseInt(br.readLine());
        int N[] = new int[205];

        StringTokenizer st = new StringTokenizer(br.readLine()," ");
        for(int i = 0; i < num; i++) {
            N[Integer.parseInt(st.nextToken())+100]++;
        }

        System.out.print(N[Integer.parseInt(br.readLine())+100]);
        br.close();
    }
}