#include <string>
#include <vector>

using namespace std;

int solution(string s) {
    int len = s.size();
    int answer = len;
    
    string str1;
    string str2;
    string str_final;
    
    int idx;
    int num;
    for(int i = 1; i <= len / 2; i++){
        num = 1;
        str1 = s.substr(0,i);
        str_final = "";
        idx = i;
        while(idx + i <= len){
            str2 = s.substr(idx,i);
            idx += i;
            if(str1 == str2){
                num += 1;
            }
            else {
                if(num > 1)
                    str_final += to_string(num);
                str_final += str1;
                str1 = str2;
                str2 = s.substr(idx,i);
                num = 1;
            }
        }
        if(num > 1)
            str_final += to_string(num);
        str_final += str1;
        str_final += s.substr(idx);
        
        if(str_final.size() < answer)
            answer = str_final.size();
    }
    
    return answer;
}