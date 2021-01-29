#include <vector>
#include <cmath>

using namespace std;

int solution(vector<int> numbers, int target) {
    int answer = 0;
    int num;
    for(int i = 0; i < pow(2, numbers.size()); i++){
        num = 0;
        for(int j = 0; j < numbers.size(); j++){
            if(i % (int) pow(2, j+1) >= pow(2,j))
                num += numbers[j];
            else
                num -= numbers[j];   
        }
        if(num == target)
               answer += 1;
    }
    
    return answer;
}