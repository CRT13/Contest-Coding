#include <bits/stdc++.h>
// #include <unordered_map>
using namespace std;

main(){
    // freopen("input.txt", "r", stdin);
	ios_base::sync_with_stdio(0);
	cin.tie(0);
	
	int n, ans=0;
	cin>>n;
	unordered_map<string,int> mp;
	string s;
	for(int i=0; i<n; ++i){
		cin>>s;
		++mp[s];
	}
	for(int i=0; i<n; ++i){
		cin>>s;
		if(mp[s]>0)
			--mp[s];
		else
			++ans;
	}
	cout<<ans;
}