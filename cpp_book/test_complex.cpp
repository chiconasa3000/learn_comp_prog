#include <iostream>
#include <cmath>
using namespace std;


class Complex{
  private:
    pair<double, double> cnumber;

  public:
    Complex(double re, double im){
      cnumber.first = re;
      cnumber.second = im;
    }
    Complex(pair<double, double> c){
      cnumber.first = c.first;
      cnumber.second = c.second;
    };
    double real(){
      return cnumber.first;
    }
    double imag(){
      return cnumber.second;
    }

   
    friend ostream& operator<<(ostream&os, Complex f){
      os <<  "[" << f.real() << "," << f.imag() << "]" << "\n";
      return os;
    }

};

//sqrt
Complex csqrt(Complex tc){

  double re = tc.real();
  double im = tc.imag();
  
  double sqrt_re = 0;
  double sqrt_im = 0;
  
  sqrt_re = sqrt((re + sqrt(pow(re,2) + pow(im,2)))/2);
  if(im < 0)
    sqrt_im = - sqrt((-re + sqrt(pow(re,2) + pow(im,2)))/2);
  else
    sqrt_im = sqrt((-re + sqrt(pow(re,2) + pow(im,2)))/2);


  return Complex(sqrt_re,sqrt_im);
}


int main(){
  //pair<double,double> p1 = make_pair(1,3);
  Complex tcomp = Complex(1,3);
  auto nc = csqrt(tcomp);
  cout << nc;
}


