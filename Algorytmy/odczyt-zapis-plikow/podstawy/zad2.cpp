#include <fstream>
#include <string>
#include <cstdlib>
using namespace std;   
    
int main()
{
    int min=30000, max=0, nr_lini=1, liczba;
    string linia;
    bool liczba_pierwsza = true;
    fstream plik1, plik2;
    plik1.open("dane_1.txt", ios::in);
    plik2.open("wynik_1.txt", ios::out | ios::app);
    while (getline(plik1,linia))
    {
    	liczba=atoi(linia.c_str());
    	for(int i=2;i<liczba;i++)
    	{
    		if (liczba % i == 0)
			{
				liczba_pierwsza = false;
			}
		}
		if (liczba_pierwsza == true)
		{
			if (liczba > max) max=liczba;
			else if (liczba < min) min=liczba;
		}
		liczba_pierwsza = true;
		nr_lini++;
    }
    plik2<<"zad 2"<<endl<<"najmniejsza liczba pierwsza: "<<min<<endl<<"najwieksza liczba pierwsza: "<<max<<endl;
}
