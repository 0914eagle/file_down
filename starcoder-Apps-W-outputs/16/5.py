
#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <cmath>
#include <vector>
#include <set>
#include <map>
#include <unordered_set>
#include <unordered_map>
#include <queue>
#include <ctime>
#include <cassert>
#include <complex>
#include <string>
#include <cstring>
#include <chrono>
#include <random>
#include <bitset>
using namespace std;

#ifdef LOCAL
	#define eprintf(...) fprintf(stderr, __VA_ARGS__)
#else
	#define eprintf(...) 42
#endif

typedef long long ll;
typedef pair<int, int> pii;
typedef pair<ll, int> pli;
typedef pair<ll, ll> pll;
typedef long double ld;
#define mp make_pair
mt19937 rng(chrono::steady_clock::now().time_since_epoch().count());

const int N = 2e5 + 10;

double x, y, r, x0, y0;

int main() {
	//ios::sync_with_stdio(false);
	//cin.tie(0);
	scanf("%lf %lf %lf %lf %lf", &r, &x, &y, &x0, &y0);
	if (r < hypot(x0 - x, y0 - y)) {
		printf("%.10f %.10f %.10f", x, y, r);
		return 0;
	}
	x = x0;
	y = y0;
	printf("%.10f %.10f %.10f", x, y, r);
	return 0;
}
