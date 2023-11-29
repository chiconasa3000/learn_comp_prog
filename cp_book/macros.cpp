#include <iostream>
#include <vector>
#include <stdio.h>
using namespace std;

#define F first
#define S second
#define PB push_back
#define MP make_pair

#define REP(i,a,b) for (int i=a; i<=b; i++)
#define SQ(a) (a)*(a)
typedef vector<pair<int,int>> vi;

int main()
{
	vi nums = vi({MP(6,4),MP(4,6)});
	nums.PB(MP(3,4));
	cout << "first: " << nums[0].F << "\n";
	cout << "second: " << nums[0].S << "\n";
	REP(i,5,20){
		cout << i << " ";
	}
	cout << "\nSQ: " << SQ(4+5) << "\n";
	return 0;
}
