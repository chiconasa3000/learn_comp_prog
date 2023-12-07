
#include "Vector.h"
#include <iostream>
#include <cmath>
using namespace std;

//sqrt function
double sqrt_sum(Vector& v){
  double sum = 0;
  for(int i = 0; i != v.size(); ++i)
    sum += sqrt(v[i]);
  return sum;
}

int main(){
  Vector vv(4);
  vv[0] = 1;
  vv[1] = 2;
  cout << "sqrt sum from: " << vv[0] << "," <<  vv[1] << " is: " << sqrt_sum(vv) << "\n";

}



