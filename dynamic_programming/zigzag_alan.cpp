// from @Alan G -> skelkjd (topcoder user)

#include <string>
#include <vector>
#include <sstream>
#include <algorithm>
#include <iostream>

using namespace std;

class ZigZag{
    public:
    int longestZigZag(vector <int> sequence){
        if(sequence.size() == 1) return 1;
        vector<int> v(sequence.size()-1);
        for(int i=1;i<sequence.size();i++){
            v[i-1] = sequence[i] - sequence[i-1];
        }
        int ii=0;
        while(ii < v.size() && v[ii] == 0)
            ii++;
        if(ii == v.size()) return 1;
        int dir = v[ii];
        int len = 2;
        for(int i=ii+1; i<v.size();i++){
            if(v[i]*dir<0){
                dir *= -1;
                len++;
            }
        }
        return len;

    }
};
int main(){
    vector<int> vect{374, 40, 854, 203, 203, 156, 362, 279, 812, 955, 600, 947, 978, 46, 100, 953, 670, 862, 568, 188, 67, 669, 810, 704, 52, 861, 49, 640, 370, 908, 477, 245, 413, 109, 659, 401, 483, 308, 609, 120, 249, 22, 176, 279, 23, 22, 617, 462, 459, 244};
    ZigZag zigzag;
    cout << zigzag.longestZigZag(vect);
}