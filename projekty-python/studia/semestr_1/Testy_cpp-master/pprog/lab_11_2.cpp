#include <iostream>
#include <cmath>

using namespace std;

double f(double x) {
    return ((3 * (x * x)) + (2 * x) - 4);
    //  x1 = 0,87 x2 = -1,54 
}



double przedzial1(double p1, double q1, int& poziom) {
    if (f(p1) == 0) return p1;
    if (poziom == 600) return p1;
    poziom++;
    double srodek = abs(p1 - q1) / 2;
    if (f(srodek) > 0) return przedzial1(p1, srodek, poziom);
    else return przedzial1(srodek, q1, poziom);
}



double x(double x) {
    return ((3 * (x * x)) + (2 * x) - 7);
    //  x1 = 0,87 x2 = -1,54 
}

double przedzial2(double p1, double q1, int& poziom) {
    if (x(p1) == 0) return p1;
    if (poziom == 600) return p1;
    poziom++;
    double srodek = abs(p1 - q1) / 2;
    if (x(srodek) > 0) return przedzial2(p1, srodek, poziom);
    else return przedzial2(srodek, q1, poziom);
}




int main(void) {

    short p1 = 0, q1 = 8;
    if(q1){
        
    }
    // p1 ma być mniejsze od q1
    int poziom = 0;
    double wynik = przedzial1(p1, q1, poziom);
    cout << wynik << "\n";
    cout << poziom << "\n";
    poziom = 0;
    wynik = przedzial2(p1, q1, poziom);
    cout << wynik << "\n";
    cout << poziom;
}