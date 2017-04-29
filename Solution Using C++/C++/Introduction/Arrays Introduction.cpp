#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;


int main() {
   int n;
   cin>>n;
   int myArray[n],c;
for(int i=0;i<n;i++){
    cin>>c;
    myArray[i]=c;
}    
    for(int j=n-1;j>=0;j--){

    cout<<myArray[j]<<" ";
}
    return 0;
}

