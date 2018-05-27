#include <algorithm>
#include <iostream>
#include <vector>
#include <map>
using namespace std;

// int get_majority_element(vector<int> &a, int left, int right) {
//   if (left == right) return -1;
//   if (left + 1 == right) return a[left];
//   //write your code here
//   return -1;
// }

int get_majority_element(vector<int> &a) { 
  map<int,int> m;
  for (int i = 0; i < a.size(); i++)
  {
    m[a[i]]++;
  }
  // cout << "map size " << m.size() << "\n";
  int n = a.size() / 2;
  // cout << n << "\n";
  // for (map<int,int>::iterator it = m.begin(); it != m.end(); it++)
  // {
  //     cout << it->first << ' ' << it->second << ' ' << n << "\n";
  // }
  for (map<int,int>::iterator it = m.begin(); it != m.end(); it++)
  {
    if (it->second > n)
      {
        return 1;
      } 
  }
  return 0;
}

int main() {
  int n;
  std::cin >> n;
  vector<int> a(n);
  for (size_t i = 0; i < a.size(); ++i) {
    std::cin >> a[i];
  }
  std::cout << get_majority_element(a) << '\n';
}
