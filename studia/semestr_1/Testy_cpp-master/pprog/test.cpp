#include <cstdlib>
#include <iostream>
using namespace std;

int main(){
    int * wsk1 =new int [10];
    int * wsk2 =new int [10];
    int * wsk3 =new int [10];
    delete [] wsk1;
    cout<<"dziala";
    wsk1 = wsk2;
}