#include <map>
#include <string>
#include <vector>
#include <cstdlib>
#include <algorithm>

using namespace std;

int solution(int n, vector<string> data) {
    int answer = 0;
    vector<char> characters = {'A', 'C', 'F', 'J', 'M', 'N', 'R', 'T'};

    do {
        map<char, int> position;
        for (int i = 0; i < characters.size(); i++)
            position[characters[i]] = i;

        bool check = true;
        for (string condition : data) {
            char x = condition[0];
            char y = condition[2];
            char op = condition[3];
            int range = condition[4] - '0';
            int dist = abs(position[x] - position[y]) - 1;

            if (op == '=') {
                if (dist != range)
                    check = false;
            }
            else if (op == '<') {
                if (dist >= range)
                    check = false;
            }
            else if (op == '>') {
                if (dist <= range)
                    check = false;
            }
            if (!check)
                break;
        }
        if (check)
            answer += 1;

    } while (next_permutation(characters.begin(), characters.end()));

    return answer;
}