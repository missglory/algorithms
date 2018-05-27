#include <algorithm>
#include <iostream>
#include <vector>
#if defined(__unix__) || defined(__APPLE__)
#include <sys/resource.h>
#endif
using namespace std;
typedef long long ll;
struct Node {
  ll key;
  int left;
  int right;

  Node() : key(0), left(-1), right(-1) {}
  Node(ll key_, int left_, int right_) : key(key_), left(left_), right(right_) {}
};

bool f = 0;

int in_order(const Node node, const vector<Node> &tree, vector<pair<ll, Node> >&x, ll depth, ll min, ll max) {
  if (node.key < min || node.key >= max ||
      (node.left != -1 && tree[node.left].key >= node.key) || 
      (node.right != -1 && tree[node.right].key < node.key))
  {
    f = 1;
    return -1;
  }
  if (node.left != -1)
    in_order(tree[node.left], tree, x, depth+1, min, node.key);
  x.push_back(make_pair(depth, node));
  // if (node.key <= tree[node.left].key) {
    // x.clear();
    // x.push_back(make_pair(depth, Node(1e15,-1,-1)));
    // x.push_back(make_pair(depth, Node(-1e15,-1,-1)));
    // return -1;
  // }
  if (node.right != -1)
    in_order(tree[node.right], tree, x, depth+1, node.key, max);
}

int nodes;

bool IsBinarySearchTree(const vector<Node>& tree) {
  // Implement correct algorithm here
  vector<pair<ll,Node> > x;
  if (tree.size() == 0) return 1;
  in_order(tree[0], tree, x, 0, -2e10, 2e10);
  // for (int i = 0; i < x.size(); i++) {
  //   cout << x[i].key << ' ';
  // }
  // cout << "\n";
  if (f) return 0;
  if (nodes != x.size()) return 0;
  for (int i = 1; i < x.size(); i++) {
    // cout << "x[i-1]:" << " first " << x[i-1].first << "\n"
    //     << "second " << x[i-1].second.key << ' ' << x[i-1].second.left << ' ' << x[i-1].second.right << "\n";
    // cout << "x[i]:" << " first " << x[i].first << "\n"
    //     << "second " << x[i].second.key << ' ' << x[i].second.left << ' ' << x[i].second.right << "\n";
        
    // if (x[i - 1].second.key > x[i].second.key)
    //   return 0;
    // if (x[i-1].second.key == x[i].second.key && x[i-1].first >= x[i].first)
    //   return 0;
  }
  return true;
}

int main() {
  #if defined(__unix__) || defined(__APPLE__)
  // Allow larger stack space
  const rlim_t kStackSize = 64 * 1024 * 1024;   // min stack size = 16 MB
  struct rlimit rl;
  int result;

  result = getrlimit(RLIMIT_STACK, &rl);
  if (result == 0)
  {
      if (rl.rlim_cur < kStackSize)
      {
          rl.rlim_cur = kStackSize;
          result = setrlimit(RLIMIT_STACK, &rl);
          if (result != 0)
          {
              std::cerr << "setrlimit returned result = " << result << std::endl;
          }
      }
  }

#endif
  // int nodes;
  std::ios_base::sync_with_stdio(0);
  cin >> nodes;
  vector<Node> tree;
  for (int i = 0; i < nodes; ++i) {
    int key, left, right;
    cin >> key >> left >> right;
    tree.push_back(Node(key, left, right));
  }
  if (IsBinarySearchTree(tree)) {
    cout << "CORRECT" << endl;
  } else {
    cout << "INCORRECT" << endl;
  }
  return 0;
}
