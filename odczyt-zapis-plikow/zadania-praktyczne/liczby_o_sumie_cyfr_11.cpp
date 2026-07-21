#include <fstream>
#include <string>
#include <cstdlib>
using namespace std;


int main(){
    int nr_lini=1, liczba,ilosc=0,pomocnicza;
    string linia;
    fstream plik1, plik2;
    plik1.open("dane_4.txt", ios::in);
    plik2.open("wynik_4.txt", ios::out | ios::app);
    plik2<<"zad 3"<<endl;
    while (getline(plik1,linia))
    {
    	liczba=atoi(linia.c_str());
	    while (liczba>1)
	    {
	    	pomocnicza+=liczba%10;
		    liczba/=10;
	    }
        if(pomocnicza==11) ilosc++;
        pomocnicza=0;
        nr_lini++;
    }
    plik2<<ilosc<<endl;
}