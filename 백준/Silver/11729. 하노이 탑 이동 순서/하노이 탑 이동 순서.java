import java.io.*;

public class Main {
    static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        
        bw.write((int)(Math.pow(2, N) - 1) +"\n");
        
        Hanoi(N, 1, 2, 3);
        
		bw.flush();
		bw.close();
    }

    public static void Hanoi(int n, int start, int mid, int dest) throws IOException {
        if(n == 1) 
            bw.write(start+" "+dest+"\n");
        else {
            Hanoi(n-1,start,dest,mid);
            bw.write(start+" "+dest+"\n");
            Hanoi(n-1,mid,start,dest);
        }
    }
}
