import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String s = br.readLine();
        int num = 0;

        for (int i = 0; i < s.length(); i++) {
            if (s.charAt(i) == 'c' && i < s.length() - 1) {
                if (s.charAt(i + 1) == '=' || s.charAt(i + 1) == '-') i++;
            } else if (s.charAt(i) == 'd' && i < s.length() - 1) {
                if (s.charAt(i + 1) == '-') i++;
                else if (s.charAt(i + 1) == 'z' && i < s.length() - 2) {
                    if (s.charAt(i + 2) == '=') i += 2;
                }  
            } else if ((s.charAt(i) == 'l' || s.charAt(i) == 'n') && i < s.length() - 1) {
                if (s.charAt(i + 1) == 'j') i++;
            } else if ((s.charAt(i) == 's' || s.charAt(i) == 'z') && i < s.length() - 1) {
                if (s.charAt(i + 1) == '=') i++;
            }
            num++;
        }
        System.out.print(num);
    }
}