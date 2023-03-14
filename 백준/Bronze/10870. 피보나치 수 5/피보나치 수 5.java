import java.io.*;

public class Main { 
    public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int N = Integer.parseInt(br.readLine());
        int [] ary = new int[N+1];
        
        if(N == 0) 
            System.out.print('0');
        else if(N == 1)
            System.out.print('1');
        else {
            ary[0] = 0; 
            ary[1] = 1;
            for(int i = 2; i<N+1; i++) {
                ary[i] = ary[i-1] + ary[i-2];
            } 
            System.out.print(ary[N]);
        }
    } 
}