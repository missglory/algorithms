#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>
using namespace std;

void pvec(vector<int> &a) {
  for (vector<int>::iterator i = a.begin(); i !=a.end(); i++)
    cout << *i << ' ';
  cout << "\n";
}


class HeapBuilder {
 public:
  vector<int> data_;
  vector< pair<int, int> > swaps_;

  void WriteResponse() const {
    cout << swaps_.size() << "\n";
    for (int i = 0; i < swaps_.size(); ++i) {
      cout << swaps_[i].first << " " << swaps_[i].second << "\n";
    }
  }

  void ReadData() {
    int n;
    cin >> n;
    data_.resize(n);
    for(int i = 0; i < n; ++i)
      cin >> data_[i];
  }

  int FirstChild(int i) { return min((unsigned int)data_.size() - 1, (unsigned)2*i + 1); }
  int SecondChild(int i) { return min((unsigned int)data_.size() - 1, (unsigned)2*i + 2); }
  int Parent(int i) { return (i - 1) / 2; }
  void SiftDown(int i) {
    while (data_[FirstChild(i)] < data_[i] || data_[SecondChild(i)] < data_[i])
    {
      if (i > data_.size()/2) return;
      if (data_[FirstChild(i)] < data_[SecondChild(i)]) {
        swap(data_[i], data_[FirstChild(i)]);
        swaps_.push_back(make_pair(i, FirstChild(i)));
        i = FirstChild(i);
      } else {
        swap(data_[i], data_[SecondChild(i)]);
        swaps_.push_back(make_pair(i, SecondChild(i)));
        i = SecondChild(i);
      }
    }
  }

  void GenerateSwaps() {
    swaps_.clear();
    // The following naive implementation just sorts 
    // the given sequence using selection sort algorithm
    // and saves the resulting sequence of swaps.
    // This turns the given array into a heap, 
    // but in the worst case gives a quadratic number of swaps.
    //
    // TODO: replace by a more efficient implementation
    // for (int i = 0; i < data_.size(); ++i)
    //   for (int j = i + 1; j < data_.size(); ++j) {
    //     if (data_[i] > data_[j]) {
    //       swap(data_[i], data_[j]);
    //       swaps_.push_back(make_pair(i, j));
    //     }
    //   }
    for (int i = data_.size() / 2 - 1; i >= 0; i--)
    {
      SiftDown(i);
    }
  }

 public:
  void Solve() {
    ReadData();
    GenerateSwaps();
    WriteResponse();
  }
};

int main() {
  std::ios_base::sync_with_stdio(false);
  HeapBuilder h;
  // h.ReadData();
  // h.SiftDown(1);
  // h.SiftDown(0);
  // h.WriteResponse();
  h.Solve();
  return 0;
}
