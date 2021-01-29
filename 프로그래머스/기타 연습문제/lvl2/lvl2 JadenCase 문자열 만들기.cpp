#include <string>
#include <vector>

using namespace std;

string solution(string s) {
    string answer = "";
    char prev = ' ';
    for(char i : s){
        if(prev == ' ')
            answer += toupper(i);
        else
            answer += tolower(i);
        prev = i;
    }
    return answer;
}