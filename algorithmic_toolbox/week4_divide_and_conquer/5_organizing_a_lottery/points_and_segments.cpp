#include <iostream>
#include <vector>
#include <algorithm>
using std::vector;
using namespace std;
#define fori for (int i = 0; i < N; i++)

bool comp(pair<int,int>a, pair<int,int> b)
{
  return 1 ? a.first < b.first : 0;
}

void printvec(vector<int> &a)
{
//   for(vector<int>::iterator i = a.begin(); i != a.end(); i++)
//   {
//     cout << *i << ' ';
//   }
//   cout << "\n";
}

void printvec(vector<pair<int, int> >&a)
{
  // for(vector<pair<int, int> >::iterator i = a.begin(); i != a.end(); i++)
  // {
  //   cout << '(' << i->first << ", " << i->second << "), ";
  // }
  // cout << "\n";
}



int main() {
  int n, m;
  std::cin >> n >> m;
  vector<int> starts(n), ends(n);
  // map<int, int > M1, M2;
  // int c = 0, d= 0;
  for (size_t i = 0; i < starts.size(); i++) {
    std::cin >> starts[i] >> ends[i];
    // M1[starts[i]] = ++c;
    // M2[ends[i]] = ++d;
  }
  
  vector<int> points(m);
  vector<int> po(points.size());
  for (size_t i = 0; i < points.size(); i++) {
    std::cin >> points[i];
  }
  // vector<pair<int, int > > pp(points.size());
  vector<int> pp(points.size() + 1);
  for (int i = 0; i < pp.size(); i++)
  {
  //   pp[i].first = points[i];
    pp[i] = 0;
  }
  vector<pair<int, int> > pi(points.size());
  for (int i = 0; i < pi.size(); i++)
  {
    pi[i].first = points[i];
    pi[i].second = i;
  }
  sort(pi.begin(), pi.end(), comp);
  sort(points.begin(), points.end());
  printvec(pi);
  printvec(points);
  for (int i = 0; i < starts.size(); i++)
  // for (vector<int>::iterator it = upper_bound(starts.begin(), starts.end(), ))
  {
    vector<int>::iterator its = lower_bound(points.begin(), points.end(), starts[i]);
    vector<int>::iterator ite = upper_bound(points.begin(), points.end(), ends[i]);
    // cout << "it start " << *its << " it end" << *ite << ' ' << starts[i] << ' ' << ends[i] << "\n";
    // for (vector<int>::iterator it = its; it != ite; it++)
    // cout << "dist " << (int)distance(points.begin(), its) << ' ' << distance(points.begin(), ite) << "\n";
    // {
      // *it++;
      // *it = *it + 1;
      pp[distance(points.begin(), its)]++;
      pp[distance(points.begin(), ite)]--;
    // }
  }
  // cout << "PP ";
  printvec(pp);
  int N = points.size();

  for (int i = 0; i < points.size(); i ++)
  {
    pi[i].first = pi[i].second;
    pi[i].second = pp[i];
  }
  // cout << "pi 1 ";
  printvec(pi);
  // sort(pi.begin(), pi.end(), comp);
  // cout << "pi ";
  // printvec(pi);
  long long ch = 0;
  // vecot <int> ans(N);
  for (int i = 0; i < pi.size(); i++)
  {
    ch += pi[i].second;
    // ans[i] = ch;
    pi[i].second = ch;
  }
  sort(pi.begin(), pi.end(), comp);
  fori{
    cout << pi[i].second << ' ';
  }

  //use fast_count_segments
  // vector<int> cnt = naive_count_segments(starts, ends, points);
  // for (size_t i = 0; i < cnt.size(); i++) {
  //   std::cout << cnt[i] << ' ';
  // }
}
