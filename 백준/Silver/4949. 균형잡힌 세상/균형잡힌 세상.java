import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);

        while (true) {
            String s = in.nextLine();

            if (s.charAt(0) == '.') break;
            System.out.println(result(s));
        }
    }

    static String result(String s) {
        Stack<Character> stack = new Stack<>();

        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);

            if (c == '(' || c == '[') stack.push(c);
            else if (c == ')') {
                if (stack.empty()) return "no";
                else if (stack.peek() != '(') return "no";
                else stack.pop();
            } else if (c == ']') {
                if (stack.empty()) return "no";
                else if (stack.peek() != '[') return "no";
                else stack.pop();
            }
        }

        if (stack.empty()) return "yes";
        else return "no";
    }
}