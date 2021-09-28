import java.util.*;

class Solution {
    public int[] solution(int[] numbers) {
        Set<Integer> set = new TreeSet<Integer>();
        for(int a = 0; a < numbers.length; a++){
            for(int b = a + 1; b < numbers.length; b++){
                set.add(numbers[a] + numbers[b]);
            }
        }

        int[] answer = new int[set.size()];
        int i = 0;
        for (Integer integer : set) {
            answer[i] = integer;
            i++;
        }
        System.out.println();
        return answer;
    }
}