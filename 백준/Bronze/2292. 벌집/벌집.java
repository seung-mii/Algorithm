
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        int count = 1;
        // 1 6 12 18 24
        if(n != 1) { // 21
            int temp = 7;
            while(true) {
                count++; //3
                if(temp >= n )
                    break;
                temp += (6*count); //37
            }
        }
        System.out.print(count);
    }
}