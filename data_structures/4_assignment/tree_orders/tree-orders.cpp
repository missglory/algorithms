#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>
#if defined(__unix__) || defined(__APPLE__)
#include <sys/resource.h>
#endif
using namespace std;

class TreeOrders {
  int n;
  vector <int> key;
  vector <int> left;
  vector <int> right;

public:
  void read() {
    cin >> n;
    key.resize(n);
    left.resize(n);
    right.resize(n);
    for (int i = 0; i < n; i++) {
      cin >> key[i] >> left[i] >> right[i];
    }
  }


  int pre_order_step(int node, vector<int> &x) {
    x.push_back(key[node]);
    if (left[node] != -1)
      pre_order_step(left[node], x);
    if (right[node] != -1) 
      pre_order_step(right[node], x);
    return node;
  }
  
  int post_order_step(int node, vector<int> &x) {
    if (left[node] != -1)
      post_order_step(left[node], x);
    if (right[node] != -1) 
      post_order_step(right[node], x);
    x.push_back(key[node]);
    return node;
  }

  int broad_order_step(int node, vector<int> &x) {
    queue<int> q;
    do {
      if (left[node] != -1)
        q.push(left[node]);
      if (right[node] != -1)  
        q.push(right[node]);
      x.push_back(key[node]);
      node = q.front();
      q.pop();
    } while(!q.empty());
    x.push_back(key[node]);
  }

  int in_order_step(int node, vector<int> &x) {
    if (left[node] != -1)
      in_order_step(left[node], x);
    x.push_back(key[node]);
    if (right[node] != -1)
      in_order_step(right[node], x);
  } 

  vector <int> in_order() {
    vector<int> result;
    // Finish the implementation
    // You may need to add a new recursive method to do that
    in_order_step(0, result);
    return result;
  }

  vector <int> pre_order() {
    vector<int> result;    
    // Finish the implementation
    // You may need to add a new recursive method to do that
    pre_order_step(0, result);    
    return result;
  }

  vector <int> post_order() {
    vector<int> result;
    // Finish the implementation
    // You may need to add a new recursive method to do that
    post_order_step(0, result);
    return result;
  }
};

void print(vector <int> a) {
  for (size_t i = 0; i < a.size(); i++) {
    if (i > 0) {
      cout << ' ';
    }
    cout << a[i];
  }
  cout << '\n';
}

int main_with_large_stack_space() {
  ios_base::sync_with_stdio(0);
  TreeOrders t;
  t.read();
  print(t.in_order());
  print(t.pre_order());
  print(t.post_order());
  return 0;
}

int main (int argc, char **argv)
{
#if defined(__unix__) || defined(__APPLE__)
  // Allow larger stack space
  const rlim_t kStackSize = 16 * 1024 * 1024;   // min stack size = 16 MB
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

  return main_with_large_stack_space();
}

