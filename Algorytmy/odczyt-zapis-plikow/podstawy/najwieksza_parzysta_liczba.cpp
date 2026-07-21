#include <fstream>
#include <string>
#include <cstdlib>
using namespace std;

int main(){
    int nr_lini=1, max=0,liczba;
    string linia;;
    fstream plik1, plik2;
    plik1.open("liczby.txt", ios::in);
    plik2.open("wynik_2.txt", ios::out | ios::app);
    while (getline(plik1,linia)){
        if (atoi(linia.c_str()) % 2 == 0)
        if (max < atoi(linia.c_str()))
            max = atoi(linia.c_str());
        nr_lini++;
    }
    plik2<<"zad1" <<endl<< max <<endl;
}