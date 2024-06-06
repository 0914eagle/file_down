
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
    int c;
    cin >> c;
    vector<int> days;
    for (int i = 0; i < c; i++) {
        int k;
        cin >> k;
        for (int j = 0; j < k; j++) {
            int n, d;
            cin >> n >> d;
            days[d - 1] += n;
        }
    }
    int sum = 0;
    for (int i = 0; i < 365; i++) {
        if (days[i] != 0) {
            sum += days[i];
            cout << sum << " ";
        }
    }
    return 0;
}
