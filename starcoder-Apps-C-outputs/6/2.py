
#include <iostream>
#include <stdio.h>
#include <vector>
#include <algorithm>
#include <queue>
using namespace std;
int n,ans=0x3f3f3f3f;
struct Node{
    int len;
    int dep;
    vector<int> vec;
}node[21];
int ind[21];
void dfs(int x){
    for(int i=0;i<node[x].vec.size();i++)
        dfs(node[x].vec[i]);
    for(int i=0;i<node[x].vec.size();i++)
        node[x].len=max(node[x].len,node[node[x].vec[i]].len);
    node[x].len+=node[x].dep;
}
int main(){
    cin>>n;
    for(int i=0;i<n;i++){
        cin>>node[i].dep;
        for(int j=0;j<node[i].dep;j++){
            int t;
            cin>>t;
            node[i].vec.push_back(t);
        }
    }
    for(int i=0;i<n;i++)
        dfs(i);
    for(int i=0;i<n;i++)
        ans=min(ans,node[i].len);
    cout<<ans<<endl;
    return 0;
}

