#include <iostream>
#include <vector>
#include <stdio.h>
using namespace std;

int main()
{
	float num1 = 0.452;
	float num2 = 0.4523;
	printf("%.2f\n",num1);

	// comparing decimal numbers
	// difference between both numbers should be \eps

	if(abs(num1-num2) < 1e-9){
		printf("%f, %f",num1, num2); 
	}

	//short types
	typedef long long ll;
	ll a = 123456789;
	ll b = 987654321;
	cout << a*b << "\n";

	typedef vector<int> vi;
	typedef pair<int,int> pi;
	
	vi *nums = new vi();
	pi coords = pi(4,5);

	return 0;
}
