#include <iostream>
#include <cmath>
#include <algorithm>
#include <vector>
using namespace std;
#define fori(n) for(int i = 0;i < (n);i++)
int main()
{
    int n, m;
    cin >> n >> m;
    vector<long long>a(n);
    fori(n){
        cin >> a[i];
    }
    fori(n){
        cout << a[i] << ' ';
    }
    cout << "\nnm" << n << ' ' << m << '\n';
    vector<pair<int,int> >t(m);
    fori(m){
        cin >> t[i].first >> t[i].second;
        t[i].first--; t[i].second--;
    }
    cout << "\n";
    long long M = -2e9;
    fori(n){
        M = max(M, a[i]);
    }
    fori(m){
        long long s = a[t[i].first] + a[t[i].second];
        M = max(M, s);
        a[t[i].first] = s;
        a[t[i].second] = s;
        cout << M << "\n";
    }
}