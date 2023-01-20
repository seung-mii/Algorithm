import java.io.*;
import java.util.Stack;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        String str = br.readLine();
        String[] arr = str.split("");
        int M = Integer.parseInt(br.readLine());

        Stack<String> leftStack = new Stack<String>();
        Stack<String> rightStack = new Stack<String>();

        for(int j = 0; j < arr.length; j++) { // for(String s : arr) {
            leftStack.push(arr[j]);
        }

        for(int i = 0; i < M; i++) {
            String command = br.readLine();
            char c = command.charAt(0);

            switch(c) {
                case 'L':
                    if(!leftStack.isEmpty()) rightStack.push(leftStack.pop());
                    break;
                case 'D':
                    if(!rightStack.isEmpty()) leftStack.push(rightStack.pop());
                    break;
                case 'B':
                    if(!leftStack.isEmpty()) leftStack.pop();
                    break;
                case 'P':
                    char t = command.charAt(2);
                    leftStack.push(String.valueOf(t));
                    break;
            }
        }

        while(!leftStack.isEmpty())
            rightStack.push(leftStack.pop());

        while(!rightStack.isEmpty())
            bw.write(rightStack.pop());

        bw.flush(); bw.close();
    }
}