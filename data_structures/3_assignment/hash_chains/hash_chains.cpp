#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <set>
using namespace std;
struct Query {
    string type, s;
    size_t ind;
};

class QueryProcessor {
    int bucket_count;
    // store all strings in one vector
    // vector<string> elems;
    vector<vector<string> > ht;

    size_t hash_func(const string& s) const {
        static const size_t multiplier = 263;
        static const size_t prime = 1000000007;
        unsigned long long hash = 0;
        for (int i = static_cast<int> (s.size()) - 1; i >= 0; --i)
            hash = (hash * multiplier + s[i]) % prime;
        return hash % bucket_count;
    }

public:
    explicit QueryProcessor(int bucket_count): bucket_count(bucket_count), ht(bucket_count) {}

    Query readQuery() const {
        Query query;
        cin >> query.type;
        if (query.type != "check")
            cin >> query.s;
        else
            cin >> query.ind;
        return query;
    }

    void writeSearchResult(bool was_found) const {
        std::cout << (was_found ? "yes\n" : "no\n");
    }

    void processQuery(const Query& query) {
#define cht ht[hash_func(query.s)]
        if (query.type == "check") {
            // use reverse order, because we append strings to the end
            // for (int i = static_cast<int>(elems.size()) - 1; i >= 0; --i)
            //     if (hash_func(elems[i]) == query.ind)
            //         std::cout << elems[i] << " ";
            // std::cout << "\n";
            for (vector<string>::iterator it = ht[query.ind].end(); it != ht[query.ind].begin(); it--){
            // for (vector<string>::iterator it = ht[query.ind].begin(); it != ht[query.ind].end(); it++){
                cout << *(--it) << ' ';
                it++;
                // cout << *it << ' ';
            }
            cout << "\n";
        } else {
            // vector<string>::iterator it = std::find(elems.begin(), elems.end(), query.s);
            vector<string>::iterator it = find(cht.begin(), cht.end(), query.s);
            if (query.type == "find") {
                // writeSearchResult(it != elems.end());
                writeSearchResult(it != cht.end());
            }
            else if (query.type == "add") {
                // if (it == elems.end())
                //     elems.push_back(query.s);
                // ht[hash_func(query.s)].insert(query.s);
                if (it == cht.end()){
                    cht.push_back(query.s);
                }
            } else if (query.type == "del") {
                if (it != cht.end())
                    cht.erase(it);
                // ht[hash_func(query.s)].erase(query.s);
            }
#undef cht
        }
    }

    void processQueries() {
        int n;
        cin >> n;
        for (int i = 0; i < n; ++i)
            processQuery(readQuery());
    }
};

int main() {
    std::ios_base::sync_with_stdio(false);
    int bucket_count;
    cin >> bucket_count;
    QueryProcessor proc(bucket_count);
    proc.processQueries();
    return 0;
}
