import java.util.*;

class Solution {
    public int[] solution(int[] numbers) {
        TreeSet<Integer> treeSet = new TreeSet<>();

        for(int i = 0; i < numbers.length - 1; i++){
            for(int j = i + 1; j < numbers.length; j++){
                treeSet.add(numbers[i] + numbers[j]);
            }
        }
        
        return Arrays.stream(treeSet.toArray(new Integer[0])).mapToInt(Integer::intValue).toArray();
    }
}