#include <fstream>
#include <string>
#include <cstdlib>
using namespace std;

int main(){
    int nr_lini=1, odwrocona=0,i;
    string linia;;
    fstream plik1, plik2;
    plik1.open("liczby.txt", ios::in);
    plik2.open("wynik_2.txt", ios::out | ios::app);
    plik2<<"zad2\n"<<endl;
    while (getline(plik1,linia)){
        i = atoi(linia.c_str());
	    while (i>1)
	    {
	    	odwrocona+=i%10;
		    if (i>10) odwrocona*=10;
		    i/=10;
	    }
        if(odwrocona == atoi(linia.c_str()))
            plik2<<odwrocona<<"\n";
        odwrocona=0;
        nr_lini++;
    }
}