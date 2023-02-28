import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        int count = 0;
        int []alphabet = new int[26];

        for(int i = 0; i < N; i++) {
            String S = br.readLine();

            for(int j = 0; j < 26; j++) {
                alphabet[j] = 0;
            }
            int k = 0;
            while(k < S.length()) {
                if((alphabet[S.charAt(k)-'a'] != 0) && (S.charAt(k-1)-'a' != S.charAt(k)-'a'))
                    break;
                alphabet[S.charAt(k)-'a']++;

                if(k == S.length()-1)
                    count++;
                k++;
            }
        }

        System.out.print(count);
    }
}