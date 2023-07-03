import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        Scanner s = new Scanner(System.in);
        StringBuilder sb = new StringBuilder();
        int num = s.nextInt();

        Stack<Integer> stack = new Stack<>();
        for(int i = 0; i < num; i++) {
            String order = s.next();
            switch(order) {
                case "push":
                    int N = s.nextInt();
                    stack.push(N);
                    break;
                case "pop":
                    if(stack.isEmpty()) sb.append(-1).append("\n");
                    else sb.append(stack.pop()).append("\n");
                    break;
                case "size":
                    sb.append(stack.size()).append("\n");
                    break;
                case "empty":
                    if(stack.isEmpty()) sb.append(1).append("\n");
                    else sb.append(0).append("\n");
                    break;
                case "top":
                    if(stack.isEmpty()) sb.append(-1).append("\n");
                    else sb.append(stack.peek()).append("\n");
                    break;
            }
        }
        System.out.println(sb);
    }
}