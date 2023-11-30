#include <iostream>
#include <stdio.h>
using namespace std;

//USING STRUCTS

//struct Vector{
//	int sz; //size
//	double* elem; //pointer to vector
//};
//
////external function
////non-constant parameter v with & operator to modify data
//void vector_init(Vector& v, int s){
//	v.elem = new double[s];
//	v.sz = s;
//}
//
//double read_and_sum(int s)
//{
//	Vector v;
//	vector_init(v,s);
//	for(int i=0; i!=s; ++i)
//		cin >> v.elem[i];
//	double sum = 0;
//	for(int i=0; i!=s; ++i)
//		sum += v.elem[i];
//	return sum;
//}
//

//USING CLASSES
class Vector{
	public:
		Vector(int s): elem{new double[s]}, sz{s}{}
		double& operator[](int i){return elem[i];}
		int size(){return sz;}
	private:
		double* elem;
		int sz;

};


double read_and_sum(int s){
	Vector v(s);
	for(int i=0; i!=v.size(); ++i)
		cin >> v[i];
	double sum = 0;
	for(int i=0; i!=v.size(); ++i)
		sum += v[i];
	return sum;
}

// ENUMERATIONS
enum class Color {red, blue, green};
enum class Traffic_light {green, yellow, red};
	
Traffic_light& operator++(Traffic_light& t){
	//It should change the parameter with the new change
	//and return this change
	switch(t){
		case Traffic_light::green: return t=Traffic_light::yellow;
		case Traffic_light::yellow: return t=Traffic_light::red;
		case Traffic_light::red: return t=Traffic_light::green;
	}
	return t;
}


int main(){
	// STRUCTS
	//Vector v = Vector();
	//int ssize = 4;
	//vector_init(v, ssize);
	//cout << "vector_size: " << v.sz << "\n";
	//cout << "write " << ssize << " numbers\n";
	//int res_sum = read_and_sum(ssize);
	//cout << "sum of before items: " << res_sum << "\n";
	
	// CLASSES
	//int ssize = 4;
	//cout << "write " << ssize << " numbers\n";
	//int res_sum = read_and_sum(ssize);
	//cout << "sum of before items: " << res_sum << "\n";

	// ENUMERATIONS

	Color col = Color::red;
	Traffic_light current_light = Traffic_light::red;
	Traffic_light next_color = ++current_light;
	//cout << "next_color: " << next_color << "\n";
	if(next_color == Traffic_light::green)
		cout << "It's green color " << "\n";

	return 0;
}
