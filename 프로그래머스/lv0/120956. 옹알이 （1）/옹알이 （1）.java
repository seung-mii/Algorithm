class Solution {
    public int solution(String[] babbling) {
        int answer = 0;

        for(int i = 0; i < babbling.length; i++) {
            babbling[i] = babbling[i].replaceFirst("aya", "0");
            babbling[i] = babbling[i].replaceFirst("woo", "0");
            babbling[i] = babbling[i].replaceFirst("ye", "0");
            babbling[i] = babbling[i].replaceFirst("ma", "0");
            babbling[i] = babbling[i].replace("0", "");
            System.out.print(babbling[i] + " ");
            
            if(babbling[i].equals("")){
                answer = answer + 1;
            }
            // if(babbling[i] =) answer++;
        }

        return answer;
    }
}