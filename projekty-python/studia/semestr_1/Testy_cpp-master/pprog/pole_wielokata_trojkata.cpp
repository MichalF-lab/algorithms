#include <stdlib.h>
#include <string>
#include <iostream>
#include <cmath>
using namespace std;

struct Punkt2
{
    double x;
    double y;
};

struct wielokat
{
    int ile_scian;
    int ile_sciana_ma_punktow;
    Punkt2 ** sciany;
    double pole;
    string nazwa_obiektu;
};



double dlugosc(Punkt2 punkt_1, Punkt2 punkt_2) {
    return sqrt((punkt_1.x + punkt_2.x) * (punkt_1.x + punkt_2.x) + (punkt_1.y + punkt_2.y) * (punkt_1.y + punkt_2.y));
}

double pole__dla_trojkata(Punkt2 pierwszy,Punkt2 drugi,Punkt2 trzeci) {


    double p = dlugosc(pierwszy, drugi) + dlugosc(pierwszy, trzeci) + dlugosc(trzeci, drugi) / 2;
    double a = dlugosc(pierwszy, drugi);
    double b = dlugosc(pierwszy, trzeci);
    double c = dlugosc(trzeci, drugi);

    return (sqrt(p * (p - a) * (p - b) * (p - c)));
}

wielokat f(int ile_scian,int ile_scianq_ma_punktow, string nazwa_obiektu) {
    wielokat ten;
    ten.ile_scian = ile_scian;
    ten.ile_sciana_ma_punktow = ile_scianq_ma_punktow;
    Punkt2 cos1[ile_scian][ile_scianq_ma_punktow];

    ten.sciany = cos1;
    ten.nazwa_obiektu = nazwa_obiektu;
    return ten;
}

int main() {
    wielokat ten = f(4,4,"czworoscian");
}