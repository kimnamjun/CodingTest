#include <string>
#include <vector>

using namespace std;

vector<vector<int>> rotation90(vector<vector<int>> key){
    int size = key.size();
    vector<vector<int>> ret = key;
    for(int i = 0; i < size; i++){
        for(int j = 0; j < size; j++){
            ret[size-j-1][i] = key[i][j];
        }
    }
    return ret;
}

bool match(vector<vector<int>> key, vector<vector<int>> lock){
    int key_size = key.size();
    int lock_size = lock.size();
    
    bool chk;
    vector<vector<int>> mat;
    
    for(int x = 1 - key_size; x < lock_size ; x++){
        for(int y = 1 - key_size; y < lock_size; y++){
            chk = true;
            mat = lock;
            for(int i = 0; i < lock_size; i++){
                for(int j = 0; j < lock_size; j++){
                    if(i-x >= 0 && i-x < key_size && j-y >= 0 && j-y < key_size){
                        if(lock[i][j] + key[i-x][j-y] == 1)
                            mat[i][j] = 1;
                        else
                            mat[i][j] = 0;
                    }
                }
            }
            for(auto i : mat){
                for(auto j : i){
                    if(j == 0)
                        chk = false;
                }
            }
            if(chk)
                return true;
        }
    }
    return false;
}

bool solution(vector<vector<int>> key, vector<vector<int>> lock) {
    bool answer = false;
    
    answer = match(key, lock);
    if(answer) return answer;
    
    key = rotation90(key);
    answer = match(key, lock);
    if(answer) return answer;
    
    key = rotation90(key);
    answer = match(key, lock);
    if(answer) return answer;
    
    key = rotation90(key);
    answer = match(key, lock);
    return answer;
}