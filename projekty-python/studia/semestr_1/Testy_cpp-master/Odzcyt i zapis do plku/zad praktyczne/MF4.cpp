#include <fstream>
#include <string>
#include <cstdlib>
using namespace std;


int main(){
    int nr_lini=1,ilosc=0,c=10,a,b,liczba;
    string linia, zminna1;
    fstream plik1, plik2;
    plik1.open("dane_4.txt", ios::in);
    plik2.open("wynik_4.txt", ios::out | ios::app);
    plik2<<"zad 4"<<endl;
    while (getline(plik1,linia))
    {
        liczba=atoi(linia.c_str());
        b=c;
        while(liczba>b) b*=c;
        a = (liczba*liczba) % b ;
        if (a==liczba) ilosc++;
    }
    plik2<<ilosc;
}