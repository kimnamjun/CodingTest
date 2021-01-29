object Solution {
    def solution(num: Int): String = {
        // -1 % 2 = -1
        if(num % 2 == 0)
            return "Even";
        else
            return "Odd";
    }
}