import java.util.*;

public class Main { 
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int H = scanner.nextInt();
        int M = scanner.nextInt();
        int C = scanner.nextInt();
        
        if(C > 59) 
            H += C/60;
        
        M += C % 60; 
        if(M > 59) {        
            M -= 60;
            H++;
        }
        
        if(H > 23) 
            H -= 24;
            
        System.out.print(H+" "+M);        
    };
}