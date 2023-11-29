#include <iostream>
using namespace std;

void factorial_module(int n){
	long long x = 1;
	for(int i=2; i<= n; i++){
		x = (x%10 * i%10)%10;
		cout << "curr_x: " << x << "\n";
	}
	cout << x%2 << "\n";
}


int main()
{
	factorial_module(4);
}
