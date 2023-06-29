import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner s = new Scanner(System.in);
        int N = s.nextInt();
        int K = s.nextInt();

        Queue<Integer> q = new LinkedList<>();

        for(int i = 1; i < N+1; i++) {
            q.add(i);
        }

        int count = 0;
        System.out.print("<");
        while(!q.isEmpty()) {
            count++;

            if(q.size() == 1) {
                System.out.print(q.poll());
                break;
            }

            if(count % K == 0) System.out.print(q.poll() + ", ");
            else {
                int temp = q.poll();
                q.offer(temp);
            }
        }
        System.out.print(">");
    }
}