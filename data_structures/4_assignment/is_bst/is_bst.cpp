#include <algorithm>
#include <iostream>
#include <vector>
using namespace std;
typedef long long ll;
struct Node {
  ll key;
  int left;
  int right;

  Node() : key(0), left(-1), right(-1) {}
  Node(ll key_, int left_, int right_) : key(key_), left(left_), right(right_) {}
};

int in_order(const Node node, const vector<Node> &tree, vector<Node>&x) {
  if (node.left != -1)
    in_order(tree[node.left], tree, x);
  x.push_back(node);
  if (node.right != -1)
    in_order(tree[node.right], tree, x);
}

bool IsBinarySearchTree(const vector<Node>& tree) {
  // Implement correct algorithm here
  vector<Node> x;
  if (tree.size() == 0) return 1;
  in_order(tree[0], tree, x);
  // for (int i = 0; i < x.size(); i++) {
  //   cout << x[i].key << ' ';
  // }
  // cout << "\n";
  for (int i = 1; i < x.size(); i++) {
    if (x[i - 1].key > x[i].key)
      return 0;
  }
  return true;
}

int main() {
  int nodes;
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
