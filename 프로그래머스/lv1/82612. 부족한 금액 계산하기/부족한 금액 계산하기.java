class Solution {
    public long solution(int price, int money, int count) {
        long use = 0; //총 이용 금액
        long answer = 0;        
        
        for(int i = 1; i<count+1; i++) {
            use += (price * i);
        }        
        
        if(money - use < 0) answer = use - money;
        
        return answer;
    }
}