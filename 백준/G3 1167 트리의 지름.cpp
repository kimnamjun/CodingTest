#include <iostream>
#include <vector>
#include <stack>
#include <string.h>

using namespace std;

int n, a, b, c;
vector<pair<int, int>> node[100001];
int dist[100001];
stack<int> stk;

void DFS(int s) {
	if (dist[s] != -1)
		return;

	dist[s] = stk.top();
	for (int i = 0; i < (int) node[s].size(); i++) {
		stk.push(stk.top() + node[s][i].second);
		DFS(node[s][i].first);
		stk.pop();
	}
}

int main() {
	cin >> n;
	for (int i = 0; i < n; i++) {
		cin >> a;
		while (true) {
			cin >> b;
			if (b == -1)
				break;
			cin >> c;
			node[a].push_back(make_pair(b, c));
		}
	}
	a = b = c = 0;

	memset(dist, -1, sizeof(int) * 100001);
	stk.push(0);
	DFS(1);

	for (int i = 1; i <= n; i++) {
		if (a < dist[i]) {
			a = dist[i];
			b = i;
		}
	}


	memset(dist, -1, sizeof(int) * 100001);
	DFS(b);

	for (int i = 1; i <= n; i++) {
		if (c < dist[i])
			c = dist[i];
	}

	cout << c;

	return 0;
}