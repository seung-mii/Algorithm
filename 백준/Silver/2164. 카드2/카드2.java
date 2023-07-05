import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner s = new Scanner(System.in);
        Queue<Integer> q = new LinkedList<>();
        int N = s.nextInt();

        for(int i = 1; i < N+1; i++) {
            q.offer(i);
        }

        boolean abandon = false;
        while(true) {
            if(q.size() == 1) break;

            if(abandon == false) {
                q.poll();
                abandon = true;
            }
            else {
                int temp = q.poll();
                q.offer(temp);
                abandon = false;
            }
        }

        System.out.print(q.peek());
    }
}