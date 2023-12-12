import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        Queue<Integer> wait = new LinkedList<>();
        Stack<Integer> space = new Stack<>();

        int N = in.nextInt();
        int num = 1;

        for (int i = 0; i < N; i++) {
            wait.offer(in.nextInt());
        }

        while (!wait.isEmpty()) {
            if (wait.peek() == num) {
                wait.poll();
                num++;
            } else if (!space.isEmpty() && space.peek() == num) {
                space.pop();
                num++;
            } else space.push(wait.poll());
        }

        System.out.println(result(space, num));
    }

    static String result(Stack space, int num) {
        while (!space.isEmpty()) {
            int order = (int) space.peek();

            if (num == order) {
                space.pop();
                ++num;
            } else return "Sad";
        }
        return "Nice";
    }
}