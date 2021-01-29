#include <string>
#include <vector>

using namespace std;

int solution(int n) {
    int size = 2;
    vector<long long> fib = {0, 1};
    while(size <= n){
        fib.push_back((fib[size-2] + fib[size-1])% 1234567);
        size += 1;
    }
    return fib[n] % 1234567;
}