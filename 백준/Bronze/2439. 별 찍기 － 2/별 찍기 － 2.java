import java.util.*;
import java.io.*;

public class Main { 
    public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        
        int N = Integer.parseInt(br.readLine());
        
        for(int i = 1; i < N+1; i++) {
            for(int j = N-1; j > (i-1); j--) {
                bw.write(" ");
            }
            for(int k = 1; k < (i+1); k++) {
                bw.write("*");
            }
            bw.write("\n");
        }
        
        br.close();
        bw.flush();
        bw.close();
    } 
}