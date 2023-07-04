import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        Scanner s = new Scanner(System.in);
        StringBuilder sb = new StringBuilder();
        int num = s.nextInt();

        Deque<Integer> d = new ArrayDeque<>();
        for(int i = 0; i < num; i++) {
            String order = s.next();
            switch(order) {
                case "push_front":
                    d.offerFirst(s.nextInt());
                    break;
                case "push_back":
                    d.offerLast(s.nextInt());
                    break;
                case "pop_front":
                    if(d.isEmpty()) sb.append(-1).append("\n");
                    else {
                        int temp = d.pollFirst();
                        sb.append(temp).append("\n");
                    }
                    break;
                case "pop_back":
                    if(d.isEmpty()) sb.append(-1).append("\n");
                    else {
                        int temp = d.pollLast();
                        sb.append(temp).append("\n");
                    }
                    break;
                case "size":
                    sb.append(d.size()).append("\n");
                    break;
                case "empty":
                    if(d.isEmpty()) sb.append(1).append("\n");
                    else sb.append(0).append("\n");
                    break;
                case "front":
                    if(d.isEmpty()) sb.append(-1).append("\n");
                    else sb.append(d.peekFirst()).append("\n");
                    break;
                case "back":
                    if(d.isEmpty()) sb.append(-1).append("\n");
                    else sb.append(d.peekLast()).append("\n");
                    break;
            }
        }
        System.out.println(sb);
    }
}