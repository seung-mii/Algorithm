import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        StringBuffer sb = new StringBuffer();
        Deque<Integer> d = new LinkedList<>();
        int N = in.nextInt();

        for (int i = 0; i < N; i++) {
            int order = in.nextInt();

            switch (order) {
                case 1:
                    d.offerFirst(in.nextInt());
                    break;
                case 2:
                    d.offerLast(in.nextInt());
                    break;
                case 3:
                    if (d.isEmpty()) sb.append("-1").append("\n");
                    else sb.append(d.pollFirst()).append("\n");
                    break;
                case 4:
                    if (d.isEmpty()) sb.append("-1").append("\n");
                    else sb.append(d.pollLast()).append("\n");
                    break;
                case 5:
                    sb.append(d.size()).append("\n");
                    break;
                case 6:
                    if (d.isEmpty()) sb.append("1").append("\n");
                    else sb.append("0").append("\n");
                    break;
                case 7:
                    if (d.isEmpty()) sb.append("-1").append("\n");
                    else sb.append(d.peekFirst()).append("\n");
                    break;
                case 8:
                    if (d.isEmpty()) sb.append("-1").append("\n");
                    else sb.append(d.peekLast()).append("\n");
                    break;
            }
        }
        System.out.print(sb);
    }
}