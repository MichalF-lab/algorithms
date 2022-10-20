#include <iostream>
using namespace std;

int main() {
    void* a;
    int* b = new int{ 10 };
    *b=10;
    a = &b;
    cout << *&a;
}