#include<string>
#include <iostream>

using namespace std;

bool solution(string s)
{
    bool answer = true;

    int open = 0;
    int close = 0;
    
   for(char c : s){
       if(c == '(')
           open += 1;
       else
           close += 1;
       if(open < close){
           answer = false;
           break;
       }
   }

    if(open != close)
        answer = false;
    
    return answer;
}