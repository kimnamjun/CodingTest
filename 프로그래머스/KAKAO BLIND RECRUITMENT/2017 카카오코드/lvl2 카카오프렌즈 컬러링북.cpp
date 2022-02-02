#include <vector>

using namespace std;

int width;
int height;
int number_of_area;
int max_size_of_one_area;
vector<vector<int>> picture_g;
vector<vector<int>> board;
vector<int> area;

void paint(int x, int y, int color){
    if (x == -1 || x == width || y == -1 || y == height
            || board[y][x] != 0 || picture_g[y][x] != color)
        return;

    board[y][x] = number_of_area;

    paint(x-1, y, color);
    paint(x+1, y, color);
    paint(x, y-1, color);
    paint(x, y+1, color);
}

vector<int> solution(int m, int n, vector<vector<int>> picture) {
    width = n;
    height = m;
    number_of_area = 0;
    max_size_of_one_area = 0;
    picture_g = picture;
    board = vector<vector<int>>(m, vector<int>(n, 0));

    for (int y = 0; y < height; y++){
        for (int x = 0; x < width; x++){
            if (picture_g[y][x] && !board[y][x]){
                number_of_area += 1;
                paint(x, y, picture_g[y][x]);
            }
        }
    }

    area = vector<int>(number_of_area + 1, 0);
    for (auto row : board)
        for (auto x : row)
            area[x] += 1;

    for (int i = 1; i < area.size(); i++)
        if (max_size_of_one_area < area[i])
            max_size_of_one_area = area[i];

    return {number_of_area, max_size_of_one_area};
}