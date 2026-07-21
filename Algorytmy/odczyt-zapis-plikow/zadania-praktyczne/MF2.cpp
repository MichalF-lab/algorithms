#include <fstream>
#include <string>
#include <cstdlib>
using namespace std;


int main(){
    int nr_lini=1, liczba,max=0;
    string linia;
    fstream plik1, plik2;
    plik1.open("dane_4.txt", ios::in);
    plik2.open("wynik_4.txt", ios::out | ios::app);
    plik2<<endl<<"zad 2"<<endl;
    while (getline(plik1,linia))
    {
    	liczba=atoi(linia.c_str());
        if(liczba>max) if(liczba%2==0) max=liczba;
        nr_lini++;
    }
    plik2<<max<<endl;
}