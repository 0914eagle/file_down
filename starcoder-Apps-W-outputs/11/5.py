

#include <iostream>
using namespace std;

int main() {
	long long t, n;
	cin >> t;
	while(t--) {
		cin >> n;
		if(n == 1) cout << 0 << '\n';
		else if(n%2 == 0) cout << n/2 << '\n';
		else cout << (n+1)/2 << '\n';
	}
	return 0;
}

