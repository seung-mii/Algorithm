import java.util.*;

public class Main {
    public static void main(String[] args) {
        Stack<Integer> s = new Stack<>();
        StringBuffer sb = new StringBuffer();
        Scanner in = new Scanner(System.in);
        int N = in.nextInt();

        for (int i = 0; i < N; i++) {
            switch (in.nextInt()) {
                case 1:
                    s.push(in.nextInt());
                    break;
                case 2:
                    if(s.empty()) sb.append("-1").append("\n");
                    else sb.append(s.pop()).append("\n");
                    break;
                case 3:
                    sb.append(s.size()).append("\n");
                    break;
                case 4:
                    if(s.empty()) sb.append("1").append("\n");
                    else sb.append("0").append("\n");
                    break;
                case 5:
                    if(s.empty()) sb.append("-1").append("\n");
                    else sb.append(s.peek()).append("\n");
                    break;
            }
        }
        System.out.println(sb);
    }
}