#include <fstream>
#include <string>
#include <cstdlib>
using namespace std;


int main(){
    int nr_lini=1, liczba;
    string linia;
    fstream plik1, plik2;
    plik1.open("dane_1.txt", ios::in);
    plik2.open("wynik_1.txt", ios::out | ios::app);
    while (getline(plik1,linia))
    {
    	liczba=atoi(linia.c_str());

        nr_lini++;
    }
}