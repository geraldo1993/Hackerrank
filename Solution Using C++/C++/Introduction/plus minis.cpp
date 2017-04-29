#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

float resPos;
float resNeg;
float resZ;

int main(){
    
    int n;
    float positive,negative,zero = 0.0;
    cin >> n;
    vector<int> arr(n);
    for(int arr_i = 0;arr_i < n;arr_i++){
        cin >> arr[arr_i];
    }
    for(int arr_i = 0;arr_i < n;arr_i++){
        if(arr[arr_i] > 0){
            
            positive++;
            
        }
        else if(arr[arr_i] < 0){
            
            negative++;
            
        }
        else {
            
            zero++ ;
            
        }
        
    }
    resPos = float(positive/n);
    resNeg = float(negative/n);
    resZ= float(zero/n);
    
    cout<<resPos<<endl;
    cout<<resNeg<<endl;
    cout<<resZ<<endl;
    
    
    
    return 0;
    
}

