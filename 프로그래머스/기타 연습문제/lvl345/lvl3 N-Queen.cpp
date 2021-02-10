#include <vector>
#include <iostream>

using namespace std;

int answer, count, N;
vector<vector<int>> board;

void subtask(int x, int y){
    int ix, iy;
    
    count += 1;
    if(count == N)
        answer += 1;
    for(ix = 0; ix < N; ix++)  // 가로
        board[y][ix] += 1;
    for(iy = 0; iy < N; iy++)  // 세로
        board[iy][x] += 1;
    ix = x - min(x, y);  // 우하향대각
    iy = y - min(x, y);
    while(ix < N && iy < N){
        board[iy][ix] += 1;
        ix++;
        iy++;
    }
    ix = x + min(N - 1 - x, y);  // 우상승대각
    iy = y - min(N - 1 - x, y);
    while(ix >= 0 && iy < N){
        board[iy][ix] += 1;
        ix--;
        iy++;
    }
    board[y][x] -= 3;  // 중복 보정
    
    for(ix = 0; ix < N; ix++)
        if(y+1 < N && board[y+1][ix] == 0)
            subtask(ix, y+1);
        
    
    count -= 1;
    for(ix = 0; ix < N; ix++)
        board[y][ix] -= 1;
    for(iy = 0; iy < N; iy++)
        board[iy][x] -= 1;
    ix = x - min(x, y);
    iy = y - min(x, y);
    while(ix < N && iy < N){
        board[iy][ix] -= 1;
        ix++;
        iy++;
    }
    ix = x + min(N - 1 - x, y);
    iy = y - min(N - 1 - x, y);
    while(ix >= 0 && iy < N){
        board[iy][ix] -= 1;
        ix--;
        iy++;
    }
    board[y][x] += 3;
}

int solution(int n) {
    N = n;
    vector<int> row = vector<int>(N, 0);
    board = vector<vector<int>>(N, row);
    for(int i = 0; i < N; i++)
        subtask(i, 0);
    return answer;
}