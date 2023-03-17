import java.util.*;
import java.io.*;

public class Main { 
    public static void main(String[] args) throws IOException {
        Scanner s = new Scanner(System.in);
        int N = s.nextInt();
        int length = 0; int newNum = N; //55
        
        while(true) { 
            int first = 0;  // 10의 자리 수
            int second = 0; // 1의 자리 수
            if(newNum < 10)  // 5
               first = 0;
            else  
               first = (newNum/10); //0
            second = (newNum%10);  //5
            
            int sum = (first + second); // 5
            newNum = (second*10 + sum%10); // 55
            length++; //3
            
            if(newNum == N)  
                break; 
        } 
        
        System.out.print(length);
    } 
}