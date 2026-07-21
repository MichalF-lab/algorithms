#include <fstream>
#include <string>
#include <cstdlib>
using namespace std;

int main(){
    int nr_lini=1, sum=0,i,sumawszystkiego=0;
    string linia;;
    fstream plik1, plik2;
    plik1.open("liczby.txt", ios::in);
    plik2.open("wynik_2.txt", ios::out | ios::app);
    plik2<<"zad3\n"<<endl;
    while (getline(plik1,linia)){
        i = atoi(linia.c_str());
	    while (i>1)
	    {
	    	sum+=i%10;
            sumawszystkiego+=i%10;
		    i/=10;
	    }
        if(sum > 30)
            plik2<<atoi(linia.c_str())<<"\n";
        sum=0;
        nr_lini++;
    }
    plik2<<"\n suma cyfr "+sumawszystkiego;
}