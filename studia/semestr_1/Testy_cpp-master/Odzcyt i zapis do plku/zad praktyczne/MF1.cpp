#include <fstream>
#include <string>
#include <cstdlib>
using namespace std;


int main(){
    int nr_lini=1, liczba;
    string linia;
    fstream plik1, plik2;
    plik1.open("dane_4.txt", ios::in);
    plik2.open("wynik_4.txt", ios::out | ios::app);
    plik2<<"zad 1"<<endl;
    while (getline(plik1,linia))
    {
    	liczba=atoi(linia.c_str());
        if (liczba%5==0) plik2<<liczba<<endl;
        nr_lini++;
    }
}