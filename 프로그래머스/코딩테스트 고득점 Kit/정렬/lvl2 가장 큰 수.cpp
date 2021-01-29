#include <string>
#include <vector>
#include <algorithm>

using namespace std;

bool compare(int a, int b){
    int ab = stoi(to_string(a) + to_string(b));
    int ba = stoi(to_string(b) + to_string(a));
    return ab > ba;
}    

string solution(vector<int> numbers) {
    int areZero = 0;
    for(auto number : numbers)
        areZero += number;
    if(!areZero)
        return "0";
    
    sort(numbers.begin(), numbers.end(), compare);
    
    string answer = "";
    for(auto number : numbers)
        answer += to_string(number);
    
    return answer;
}