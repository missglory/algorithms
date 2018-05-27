#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>
using namespace std;
#define ll long long
struct thread{
  int n;
  ll time;
  thread(int w, ll t): n(w), time(t) {}
};

bool compare(thread const& a, thread const& b){
  if (a.time < b.time) return 0;
  if (a.time == b.time) return a.n > b.n;
  return 1;
}
struct comp{
  bool operator()(thread const& x, thread const &y) { return compare(x,y); }
};

void printq(priority_queue<thread, vector<thread>, comp>q){
  // priority_queue<thread, vector<thread>, comp> qq = q;
  // while (!qq.empty()){
  //   cout << qq.top().n << ' ';
  //   qq.pop();
  // }
  // cout << '\n';
  // while (!q.empty()){
  //   cout << q.top().time << ' ';
  //   q.pop();
  // }
  // cout << "\n";
}

class JobQueue {
 public:
  int num_workers_;
  vector<int> jobs_;

  vector<int> assigned_workers_;
  vector<long long> start_times_;
  priority_queue<thread, vector<thread>, comp> q;
  void WriteResponse() const {
    for (int i = 0; i < jobs_.size(); ++i) {
      cout << assigned_workers_[i] << " " << start_times_[i] << "\n";
    }
  }

  void ReadData() {
    int m;
    cin >> num_workers_ >> m;
    jobs_.resize(m);
    for(int i = 0; i < m; ++i)
      cin >> jobs_[i];
    for(int i = 0; i < num_workers_; i++){
      q.push(thread(i, 0));
    }
    printq(q);
  }

  void AssignJobs() {
    // TODO: replace this code with a faster algorithm.
    // assigned_workers_.resize(jobs_.size());
    // start_times_.resize(jobs_.size());
    // vector<long long> next_free_time(num_workers_, 0);
    // for (int i = 0; i < jobs_.size(); ++i) {
    //   int duration = jobs_[i];
    //   int next_worker = 0;
    //   for (int j = 0; j < num_workers_; ++j) {
    //     if (next_free_time[j] < next_free_time[next_worker])
    //       next_worker = j;
    //   }
    //   assigned_workers_[i] = next_worker;
    //   start_times_[i] = next_free_time[next_worker];
    //   next_free_time[next_worker] += duration;
    // }
    int jobsiter = 0;
    while (jobsiter < jobs_.size()) {
      thread a = q.top();
      assigned_workers_.push_back(a.n);
      start_times_.push_back(a.time);
      q.pop();
      q.push(thread(a.n, a.time + jobs_[jobsiter++]));
    }
  }

 public:
  void Solve() {
    ReadData();
    AssignJobs();
    WriteResponse();
  }
};

int main() {
  std::ios_base::sync_with_stdio(false);
  JobQueue job_queue;
  // job_queue.ReadData();
  job_queue.Solve();
  return 0;
}
