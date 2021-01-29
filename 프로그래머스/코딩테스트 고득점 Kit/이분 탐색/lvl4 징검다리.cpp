#include <vector>
#include <list>
#include <algorithm>

using namespace std;

int solution(int distance, vector<int> rocks, int n){
    rocks.push_back(0);
    rocks.push_back(distance);
    sort(rocks.begin(), rocks.end());
    
    list<int> dist;
    for(int i = 1; i < rocks.size(); i++)
        dist.push_back(rocks[i] - rocks[i-1]);
    
    int left = 1;
    int right = distance;
    int mid, cnt, wrong, temp;
    while(left <= right){
        cnt = wrong = 0;
        mid = (left + right) / 2;
        list<int> dist_c = list<int>(dist);
        
        for(list<int>::iterator it = dist_c.begin(); it != dist_c.end();){
            if(*it < mid){
                cnt++;
                temp = *it;
                it = dist_c.erase(it);
                *it += temp;
                if(cnt > n){
                    wrong = 1;
                    break;
                }
            }
            else
                it++;
        }
        
        if(wrong)
            right = mid - 1;
        else
            left = mid + 1;        
    }
    return right;
}