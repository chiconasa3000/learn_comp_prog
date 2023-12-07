#include "Vector.h"

Vector::Vector(int s)
  :elem{new double[s]}, sz{s}
{}

// modify or get the value in vector
double& Vector::operator[](int i){
  return elem[i];
}

int Vector::size(){
  return sz;
}


