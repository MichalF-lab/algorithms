#include <iostream>
using namespace std;

void funkcja (int *& tab){
    tab++;
}

int main(){
    int * tab = new int [3]{1,2,3};
    cout<<*tab;
    funkcja(tab);
    cout<<*tab;
}