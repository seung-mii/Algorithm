import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int N = Integer.parseInt(br.readLine());
        int[] origin = new int[N];   
        int[] sorted = new int[N];    
        int rank = 0;
        HashMap<Integer, Integer> rankingMap = new HashMap<Integer, Integer>();

        StringTokenizer st = new StringTokenizer(br.readLine(), " ");
        for (int i = 0; i < N; i++) {
            sorted[i] = origin[i] = Integer.parseInt(st.nextToken());
        }

        Arrays.sort(sorted);

        for (int v = 0; v < sorted.length; v++) {
            if (!rankingMap.containsKey(sorted[v]))
                rankingMap.put(sorted[v], rank++);
        }

        StringBuilder sb = new StringBuilder();
        for (int key = 0; key < origin.length; key++) {
            sb.append(rankingMap.get(origin[key])).append(' ');
        }

        System.out.println(sb);
    }
}