import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String [] ary = new String[Integer.parseInt(br.readLine())];
        int [] answer = new int[ary.length];

        for(int i = 0; i<ary.length; i++) {
            ary[i] = br.readLine();
        }

        for(int i =0; i<ary.length; i++) {
            int count = 0;
            int sum = 0;
            for(int j = 0; j<ary[i].length(); j++) {
                if(ary[i].charAt(j) == 'O')
                   count++;
                else
                    count = 0;
                sum += count;
            }
            answer[i] = sum;
        }

        for(int i =0; i<ary.length; i++) {
            System.out.println(answer[i]);
        }

        br.close();
    }
}