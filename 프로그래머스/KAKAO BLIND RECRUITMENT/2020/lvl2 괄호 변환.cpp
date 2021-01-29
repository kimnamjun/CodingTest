#include <string>
#include <vector>

using namespace std;

string func(string s){
    int idx = 0;
    int cnt = 0;
    string u = "";
    string v = "";
    
    if(s.empty())
        return s;
    
    do {
        if(s[idx] == '(')
            cnt += 1;
        else
            cnt -= 1;
        idx += 1;
    } while(cnt != 0);
    
    u = s.substr(0,idx);
    v = s.substr(idx);
    
    if(u[0] == '('){
        return u + func(v);
    }
    else {
        string temp1 = "(" + func(v) + ")";
        string temp2 = u.substr(1, u.size() - 2);
        string temp3 = "";
        for(auto i : temp2){
            if(i == '(')
                temp3 += ")";
            else
                temp3 += "(";
        }
        temp1 += temp3;
        return temp1;
    }
}

string solution(string p) { 
    string answer = func(p);
    return answer;
}