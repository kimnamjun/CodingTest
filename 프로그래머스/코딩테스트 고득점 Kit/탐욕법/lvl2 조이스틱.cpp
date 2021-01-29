#include <string>
#include <vector>

using namespace std;

/*
solution.py
def solution(name):
    a = [idx for idx, val in enumerate(name) if val != 'A']
    a1 = min(a[0], a[-1])  # 가장 가까운 A가 아닌 곳까지 거리
    a2 = min(a[-1] - a[0], len(name) + a[0] - a[1])  # 왼쪽이 빠른가 오른쪽이 빠른가
    a3 = sum(min(ord(n) - ord('A'), ord('Z') - ord(n) + 1) for n in name)  # 알파벳 돌리기
    return a1 + a2 + a3
*/

int solution(string name) {
    vector<int> a;
    for(int i = 0; i < name.size(); i++)
        if(name[i] != 'A')
            a.push_back(i);
    int a1 = min(a[0], a[a.size()-1]);
    
    int a2;
    if(a.size() > 1){
        int t = (name.size() + a[0] - a[1]);
        a2 = min(a[a.size()-1] - a[0], t);
    }
    else
        a2 = 0;
    
    int a3 = 0;
    for(auto n : name)
        a3 += min(n - 'A', 'Z' - n + 1);
    
    return a1 + a2 + a3;
}