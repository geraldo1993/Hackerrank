#include <iostream>
#include <cstdio>
using namespace std;


int main(){

int a,b,i;


cin>>a>>b;

    string Num[9]={"one","two","three","four","five","six","seven","eight","nine"};

for(i=a; i<=b; i++){
    if(i<10){

    cout << Num[i-1] << endl;
    }

    else if (i%2==0){

       cout << "even" << endl;

    }
     else{
        cout << "odd" <<endl;

         }

            }

return 0;

}
