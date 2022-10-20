#include <fstream>
#include <string>
#include <cstdlib>
using namespace std;   
    
int main()
{
    int nr_lini=1, liczba, ilosc_par=0,poprzednia_para;
    bool para = false;
    string linia;
    bool liczba_pierwsza = true;
    fstream plik1, plik2;
    plik1.open("dane_1.txt", ios::in);
    plik2.open("wynik_1.txt", ios::out | ios::app);
    plik2<<"zad 3"<<endl;
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
			if(para==false)
			{
				poprzednia_para = liczba;
				para=true;
				break;
			}
			if(para==true)
			{
				plik2<<poprzednia_para<<" i "<<liczba<<endl;
				ilosc_par++;
				para=false;
				break;
			}
		}
		liczba_pierwsza = true;
		nr_lini++;
    }
    plik2<<"ilosc par: "<<ilosc_par;
}
    
