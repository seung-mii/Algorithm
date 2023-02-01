import java.util.*;

class Solution {
    public int[] solution(int[] arr, int divisor) {
        List<Integer> arrayList = new ArrayList<Integer>();

        for(int i = 0; i < arr.length; i++) {
            if(arr[i] % divisor == 0) arrayList.add(arr[i]);
        }

        if(arrayList.size() == 0) arrayList.add(-1);
        int answer[] = new int[arrayList.size()];
        
        int size = 0;
        for(int temp : arrayList){
            answer[size++] = temp;     
        }
        
        Arrays.sort(answer);
        return answer;
    }
}