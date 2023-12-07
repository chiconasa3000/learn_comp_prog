
#include <iostream>
using namespace std;
// the init pivot is a
// the end pivot is b
// test different subarrays between [a,b]
// subarrays are considered in all possible sizes
// Order(n^3)

void max_subarr_sum(int array[],int n){
  int best = 0;
  for(int a = 0; a < n; a++){
    for(int b = a; b < n; b++){
      int sum = 0;
      for(int k=a; k<=b; k++){
        sum += array[k];
      }
      best = max(best, sum);
    }
  }

  cout << "best_sum_in_subarray: " << best << "\n";
}

//meanwhile change pivot b, it updates
//the best sum
//Order(n^2)
void max_subarr_sum_v2(int array[],int n){
 
  int best = 0;
  for(int a = 0; a < n; a++){
    int sum = 0;
    for(int b = a; b < n; b++){
      sum += array[b];
      best = max(best, sum);
    }
  }
  cout << "best_sum_in_subarray: " << best << "\n";
}

// Kadane's Algorithm

void max_subarr_sum_v3(int array[], int n){
  int best = 0, sum=0;
  for(int k = 0; k < n; k++){
    // if find an item which is bigger than current sum
    // update new sum (check all possible choices)
    sum = max(array[k], sum+array[k]);
    // check previous sum even if the item was bigger than
    // current sum
    best = max(best,sum);
  }

  cout << "best_sum_in_subarray: " << best << "\n";
}


int main(){
 
  int v[] = {-1,2,4,-3,5,2,-5,2};
  int len = sizeof(v)/sizeof(int);
  //max_subarr_sum(v,len);
  //max_subarr_sum_v2(v,len);
  max_subarr_sum_v3(v,len);

  return 0;
}
