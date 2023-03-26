import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String S = br.readLine();

        int []Alphabet = new int[26];
        for(int i =0; i<26; i++) {
            Alphabet[i] = -1;
        }

        for(int i =0; i<S.length(); i++) {
            int temp = S.charAt(i)-97;

            if(Alphabet[temp] == -1)
                Alphabet[temp] = i;
        }

        for(int i =0; i<26; i++) {
            System.out.print(Alphabet[i]+" ");
        }
    }
}