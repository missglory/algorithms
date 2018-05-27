#include <iostream>
#include <limits>
#include <vector>
#include <queue>
#include <string>

using std::vector;
using std::queue;
using std::pair;
using std::priority_queue;
long long inf = std::numeric_limits<long long>::max();


int BellmanFord(vector<vector<int> >&adj, vector<vector<int> > &cost, int s, vector<long long> &distance, 
                vector<bool> &reachable, vector<bool> &shortest, bool is_second = 0) {
  int n = adj.size();
  for (int k = 0; k < n - 1; k++) {
    bool f = 0;
    for (int i = 0; i < n; i++) {
      if (!reachable[i] || distance[i] >= inf) continue;
      for (int j = 0; j < adj[i].size(); j++) {
        int c = adj[i][j];
        if (!reachable[c]) continue;
        long long relax = distance[i] + cost[i][j];
        if (distance[c] > relax) {
          distance[c] = relax;
          f = 1;
          if (is_second) return c;
          shortest[c] = 0;
        } 
      }
    }
    if (!f) break;
  }
  return -1;
}


void dfs(vector<vector<int> > &adj, int x, vector<bool>&rchbl, bool filler, vector<bool> &u) {
  u[x] = 1;
  rchbl[x] = filler;
  for (int i = 0; i < adj[x].size(); i++) {
    int next = adj[x][i];
    if (!u[next]) {
      dfs(adj, next, rchbl, filler, u);
    }
  }
} 

void shortest_paths(vector<vector<int> > &adj, vector<vector<int> > &cost, int s, vector<long long> &distance, vector<bool> &reachable, vector<bool> &shortest) {
  //write your code here
  int n = adj.size();
  vector<bool> u(n, 0);
  dfs(adj, s, reachable, 1, u);
  BellmanFord(adj, cost, s, distance, reachable, shortest, 0);
  for (int i = 0; i < shortest.size(); i++) shortest[i] = 1;
  int cycle_node = BellmanFord(adj, cost, s, distance, reachable, shortest, 1);
  for (int i = 0; i < u.size(); i++) u[i] = 0;
  if (cycle_node != -1) dfs(adj, cycle_node, shortest, 0, u);
}

int main() {
  // std::string file_path = __FILE__;
  // #if defined(__unix__) || defined(__APPLE__)
  //   std::string test_path = file_path.substr(0, file_path.rfind("/")) + "/test/02";
  // #else
  //   std::string test_path = file_path.substr(0, file_path.rfind("\\")) + "/test/02";
  // #endif 
  // freopen(test_path.c_str(), "r", stdin);


  int n, m, s;
  std::cin >> n >> m;
  vector<vector<int> > adj(n, vector<int>());
  vector<vector<int> > cost(n, vector<int>());
  for (int i = 0; i < m; i++) {
    int x, y, w;
    std::cin >> x >> y >> w;
    adj[x - 1].push_back(y - 1);
    cost[x - 1].push_back(w);
  }
  std::cin >> s;
  s--;
  vector<long long> distance(n, inf);
  distance[s] = 0;
  vector<bool> reachable(n, 0);
  vector<bool> shortest(n, 1);
  shortest_paths(adj, cost, s, distance, reachable, shortest);
  for (int i = 0; i < n; i++) {
    if (!reachable[i]) {
      std::cout << "*\n";
    } else if (!shortest[i]) {
      std::cout << "-\n";
    } else {
      std::cout << distance[i] << "\n";
    }
  }
}
