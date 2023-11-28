#include <iostream>
using namespace std;

// square returning constexpr
constexpr double square(double x)
{
	return x*x;
}

/*void print_square(double x)
{
	cout << "the square of " << x <<" is: " << square(x) << "\n";
}
*/


// loop, switch
bool accept3times()
{
	int tries = 1;
	while(tries < 4){
		cout << "Do you want to proceed (y or n)?\n";
		char answer = 0;
		cin >> answer;

		switch(answer){
			case 'y':
			      return true;
			case 'n':
			      return false;
			default:
			      cout << "Sorry, I don't understand that. \n";
			      ++tries;
			  
		}
	}
	cout << "I'll take that as a no answer";
	return false;
}

//copy items from vector
void copy_fc()
{
	int v1[10] = {0,1,2,3,4,5,6,7,8,9};
	int v2[10];

	for(auto i : v1)
		v2[i] = v1[i];
	cout << "values in v2: ";
	for(auto &x : v2){
		++x;
		cout << x << " ";
	}
	cout << "\n";
	
	v1[0] = 1;	
	cout << "item_v1: " << v1[0] << " item_v2: " << v2[0] << "\n";
}

// counting

int count_x(char *p, char x)
{
	//p is assumed to point to a zero-terminated array of char (or to nothing)
	if(p == nullptr) return -1;
	int count = 0;
	for(; *p!=0; ++p)
		if(*p == x)
			++count;
	return count;
}

int main()
{
	// using a function
	//print_square(5);

	// knowing the size of variable type (bytes)
	cout << "size " << sizeof(char) << "\n";
	// initializing a value
	double d2 {2.4};
	cout << d2 << "\n";

	// declare auto variables
	auto y {4.2};
	auto z = y*y;
	
	// constants and constexpr
	const int dmv = 7;
	constexpr double dnum = square(dmv);
	cout << dnum << "\n";

	// loops, switch
	//cout << accept3times();

	//copy items
	copy_fc();

	//declaring a vector
	int v[] {0,1,2};
	int *pv = v;
	pv++;
	cout << "pointer second item: " << *pv << "\n";

	//null pointer
	double * pd = nullptr;
	cout << "nullptr: " << pd << "\n";

	//counting
	char text[] {'h','e','l','l','o','o','o','o','0'};
	char *ptext;
	cout << "counting : " << count_x(ptext,'o') << "\n";
		
}
