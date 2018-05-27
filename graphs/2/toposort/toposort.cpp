#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
using namespace std;
bool used[(int)1e3+2], removed[(int)1e3+2];
int n,m;

bool dfs(int v, vector<vector<int> >&adj, vector<int>&order){
  used[v] = 1;
  for (int i = 0; i < adj[v].size();i++){
    int next = adj[v][i];
    if (removed[next]) continue;
    if (!used[next])
      dfs(next, adj, order);
  }
  removed[v] = 1;
  order.push_back(v);
  return 1;
}   

vector<int> toposort(vector<vector<int> > adj) {
  vector<int> order;
  vector<vector<int> > adj_reverse(n);
  for (int i = 0; i < n; i++) {
    for (int j = 0; j < adj[i].size(); j++) {
      adj_reverse[j].push_back(i);
    }
  }
  for (int i = 0; i < n; i++){
    if (!removed[i]) {
      dfs(i, adj_reverse, order);
    }
  }
  for (int i = 0; i < order.size(); i++){
    cout << order[i] << ' ';
  }
  return order;
}

int main() {
  // size_t n, m;
  string file_path = __FILE__;
  string dir_path = file_path.substr(0, file_path.rfind("\\"));
  string test_path = dir_path + "\\test\\01";
  freopen(test_path.c_str(), "r", stdin);

  
  std::cin >> n >> m;
  vector<vector<int> > adj(n, vector<int>());
  for (size_t i = 0; i < m; i++) {
    int x, y;
    std::cin >> x >> y;
    adj[x - 1].push_back(y - 1);
  }
  vector<int> order = toposort(adj);
  for (size_t i = 0; i < order.size(); i++) {
    std::cout << order[i] + 1 << " ";
  }
}
