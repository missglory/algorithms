#include <iostream>
#include <vector>
#include <algorithm>
using std::vector;
using namespace std;
#define ull unsigned long long
#define int long long

void printvec(vector<int> &a)
{
  // for(vector<int>::iterator i = a.begin(); i != a.end(); i++)
  // {
  //   cout << *i << ' ';
  // }
  // cout << "\n";
}

pair<vector<int>, int> merge(vector<int> &b, vector<int> &c, 
                      // vector<int> & result, 
                      size_t l1 = 0, size_t l2 = 0, size_t r1 = 0, size_t r2 = 0){
  // int i = l;
  // int j = l;
  // if (r == 0) r = b.size();
  int i = l1;
  int j = l2;
  r1 = r1 == 0 ? b.size() : r1;
  r2 = r2 == 0 ? c.size() : r2;
  vector<int> result;
  int pairs = 0;
  while (i < r1 || j < r2)
  {
    // cout << i << " " << j << ' ' << b[i] << ' ' << c[j] << ' ' << result.size() << '\n';
    if (i >= r1)
      while (j < r2)
      {
        // cout << j << ' ' << c[j] << ' ' << result.size() << '\n';
        result.push_back(c[j++]);
      }
    if (j >= r2)
      while (i < r1)
      {
        // cout << b[i] << "\n";
        result.push_back(b[i++]);
        // pairs += (int) c.size();
        // cout << "p+ " << c.size() << "res "; printvec(result);
      }
    if (i >= r1 || j >= r2) continue;
    if (b[i] <= c[j])
    {
      result.push_back(b[i++]);
      // cout << b[i] << ' ' << "i " << i << '\n';
      // i++;
    } else {
      pairs += b.size() - i;
      // cout << "PAIRS+ " << b.size() - i << "res "; printvec(result);
      result.push_back(c[j++]);
      // cout << c[j] << ' ' << "j " << j << "\n";
    }
  }
  // cout << "size " << result.size() << "\n";
  // cout << "b "; printvec(b);
  // cout << "c "; printvec(c);
  // cout << "" << pairs << "\n\n";
  return make_pair(result, pairs);
}










    pair<vector<int>,int> 
    // int
    gni(vector<int> &a, 
              // vector<int> & aprime, 
              int l, int r)
    {
      int npairs = 0;
      if (l + 1 >= r)
      {
        // clear(aprime);
        vector<int> res;
        res.push_back(a[l]);
        return make_pair(res, npairs);
        // return npairs;
      }
      int m = (l + r) / 2;
      pair<vector<int>,int> b = gni(a, 
                       l, m);
      pair<vector<int>, int> c = gni(a, 
                    m, r);
      // vector<int> b = gni(a, l, m).first;
      // vector<int> c = gni(a, m, r).first;
      // pair<vector<int>, int> mp = merge(b, c);
      pair<vector<int>, int> mp = merge(b.first, c.first);
      vector<int> aprime = mp.first;
      npairs += mp.second;
      npairs += b.second + c.second;
      
      // cout << "state " << l << ' ' << m << ' ' << r << '\n';
      // printvec(b.first);
      // printvec(c.first);
      // cout << npairs;

      // ap.second = npairs;
      return make_pair(aprime, npairs);
    }



long long get_number_of_inversions(vector<int> &a, vector<int> &b, size_t left, size_t right) {
  long long number_of_inversions = 0;
  if (right <= left + 1) return number_of_inversions;
  size_t ave = left + (right - left) / 2;
  number_of_inversions += get_number_of_inversions(a, b, left, ave);
  number_of_inversions += get_number_of_inversions(a, b, ave, right);
  // number_of_inversions += merge(a,b,left,right).second;
  //write your code here
  vector<int> x, y;

  return number_of_inversions;
}
#undef int
int main() {
#define int long long

  int n;
  std::cin >> n;
  vector<int> a(n);
  for (size_t i = 0; i < a.size(); i++) {
    std::cin >> a[i];
  }
  // vector<int> b(a.size());
  // vector<int> b = a;
  // sort(b.begin(), b.end());
  // std::cout << get_number_of_inversions(a, b, 0, a.size()) << '\n';
  // vector<int> a;
  // a = vector<int>({1,3,5});
  // cout << "a size " << a.size() << '\n';
  //  vector<int> b({2,4,6});
  // pair <vector<int>, int> res = merge(a,b);
  // pair<vector<int>,int> ap = gni(a, 0, a.size());
  // cout << "size " << res.first.size() << '\n';
  // vector<int> ap(a.size());
  // int re = gni(a, aprime, 0, a.size());
  pair<vector<int>, int> pp = gni(a, 0, a.size());
  vector<int> ap = pp.first;
  // for (int i = 0; i < ap.size(); i ++ ){
  //   cout << ap[i] << ' ';
  // }
  // vector<int> fwg({2,3}), few({2,9,9});
  // pair<vector<int>, int> tt = merge(fwg, few);
  // cout << "MERGE " << tt.second << "\n";
  // printvec(tt.first);
  cout << pp.second << "\n";
  // cout << "\n" << ap.second << "\n";
}
