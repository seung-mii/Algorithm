import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String s = br.readLine();
        int time = 0;
        
        for(int i = 0; i<s.length(); i++) {
            int temp = s.charAt(i) - 'A';
            if(temp < 3) 
                time += 3;
            else if (temp > 2 && temp < 6) 
                time += 4;
            else if (temp > 5 && temp < 9) 
                time += 5;
            else if (temp > 8 && temp < 12) 
                time += 6;
            else if (temp > 11 && temp < 15) 
                time += 7;
            else if (temp > 14 && temp < 19) 
                time += 8;
            else if (temp > 18 && temp < 22) 
                time += 9;
            else if (temp > 21 && temp < 26) 
                time += 10;
            else 
                time += 11;
        }
        System.out.print(time);
    }
}