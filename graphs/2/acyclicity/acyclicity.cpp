#include <iostream>
#include <vector>

using namespace std;
bool used[(int)1e3+2], removed[(int)1e3+2];
int n,m;

bool dfs(int v, vector<vector<int> >&adj){
  used[v] = 1;
  for (int i = 0; i < adj[v].size();i++){
    int next = adj[v][i];
    if (removed[next]) continue;
    if (used[next] == 1)
      return 0;
    else
    // if (!used[next])
      if (!dfs(next, adj)) return 0;
  }
  removed[v] = 1;
  return 1;
}

int acyclic(vector<vector<int> > &adj) {
  for (int i = 0; i < n; i++){
    if(removed[i]) continue;
    if(!dfs(i,adj)) return 1;
  }
  return 0;
}

int main() {
  // size_t n, m;
  // freopen("C:\\Users\\Admin\\Desktop\\crsra\\graphs\\2\\acyclicity\\test\\01", "r", stdin);
  std::cin >> n >> m;
  vector<vector<int> > adj(n, vector<int>());
  for (size_t i = 0; i < m; i++) {
    int x, y;
    std::cin >> x >> y;
    adj[x - 1].push_back(y - 1);
  }
  std::cout << acyclic(adj);
  // system("PAUSE");
}
