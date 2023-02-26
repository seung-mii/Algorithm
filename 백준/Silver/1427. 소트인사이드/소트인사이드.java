import java.io.*;
import java.util.Arrays;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String strN = br.readLine();
        int n[] = new int[strN.length()];

        for(int i = 0; i < strN.length(); i++) {
            n[i] = (int)(strN.charAt(i)) - 48;
        }

        Arrays.sort(n);

        for(int i = strN.length() - 1; i > -1; i--) {
            System.out.print(n[i]);
        }

        br.close();
    }
}