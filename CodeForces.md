    Copyright (c) 2018-
    Author: Chaitanya Tejaswi (github.com/CRTejaswi)    License: GPL v3.0+

# CodeForces - Contest Problems

> Personal solutions to programming puzzles/challenges.


### [1000](https://codeforces.com/contests/1000)

[Problems](Problems/1000.pdf)

* Delete Single-Matches from both lists.
* Transform one list to another.


```python
# [A]
X1,X2 = [],[]
n = int(input())
temp = n
while(n>0):
    X1.append(input())
    n-=1
n = temp
while(n>0):
    X2.append(input())
    n-=1
# X1,X2 = np.array(X1),np.array(X2)
# Delete Single-Matches from both lists.
X1.remove(*(set(X1) & set(X2)))
X2.remove(*(set(X1) & set(X2)))
print(X1,X2,sep='\n')
```

    2
    M
    XS
    XS
    M



    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-4-a4eaf503b3b2> in <module>()
         12 # X1,X2 = np.array(X1),np.array(X2)
         13 # Delete Single-Matches from both lists.
    ---> 14 X1.remove(*(set(X1) & set(X2)))
         15 X2.remove(*(set(X1) & set(X2)))
         16 print(X1,X2,sep='\n')


    TypeError: remove() takes exactly one argument (2 given)



```python
#include <bits/stdc++.h>
using namespace std;

main(){
    freopen("input.txt", "r", stdin);
	ios_base::sync_with_stdio(0);
	cin.tie(0);

	int n, ans=0;
	cin>>n;
	unordered_map<string, int> mp;
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
```
