
#include <iostream>
using namespace std;
int n,L,d,x,ans;
int main()
{
    cin >> L >> d >> n;
    for (int i=1;i<=n;i++)
    {
        cin >> x;
        if (x<=d) ans+=d-x;
        else if (x>=L-d) ans+=x-(L-d);
    }
    cout << ans << endl;
    return 0;
}
