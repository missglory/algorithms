#include <iostream>
#include <vector>
#include <cstdlib>
using namespace std;
using std::vector;
using std::swap;

int partition2(vector<int> &a, int l, int r) {
  int x = a[l];
  int j = l;
  for (int i = l + 1; i <= r; i++) {
    if (a[i] <= x) {
      j++;
      swap(a[i], a[j]);
    }
  }
  swap(a[l], a[j]);
  return j;
}

pair<int,int> partition3(vector<int> &a, int l, int r)
{
  int j = l;
  int equals = 0;
  for (int i = l + 1; i <= r; i++)
  {
    if (a[i] == a[l])
      equals++;
    if (a[i] < a[l]) {
      j++;
      swap(a[i],a[j]);
    }
  }
  swap(a[l], a[j]);
  return make_pair(j, equals);
}

void randomized_quick_sort(vector<int> &a, int l, int r) {
  if (l >= r) {
    return;
  }

  int k = l + rand() % (r - l + 1);
  swap(a[l], a[k]);
  pair<int,int> p = partition3(a, l, r);
  int m = p.first;
  int eq = p.second;
  randomized_quick_sort(a, l, m - 1);
  randomized_quick_sort(a, m + 1 + eq, r);
}

int main() {
  int n;
  std::cin >> n;
  vector<int> a(n);
  for (size_t i = 0; i < a.size(); ++i) {
    std::cin >> a[i];
  }
  randomized_quick_sort(a, 0, a.size() - 1);
  for (size_t i = 0; i < a.size(); ++i) {
    std::cout << a[i] << ' ';
  }
}
