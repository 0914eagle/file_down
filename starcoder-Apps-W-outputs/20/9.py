
#include <iostream>
#include <vector>
using namespace std;

int main() {
    int l, d, n;
    cin >> l >> d >> n;
    vector<int> v;
    for (int i=0; i<n; i++) {
        int a; cin >> a;
        v.push_back(a);
    }
    v.push_back(0); v.push_back(l);
    int ans = 0;
    for (int i=1; i<v.size(); i++) {
        if ((v[i] - v[i-1]) - d - 6 > 0) {
            ans += ((v[i] - v[i-1]) - d - 6)/d + 1;
        }
    }
    cout << ans << endl;
    return 0;
}
