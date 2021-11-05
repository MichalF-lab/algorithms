#include <iostream>
#include <string.h>

using namespace std;

string kodCezara(string kod, int klucz)
{
	int pom;
	for (int i = 0; i < kod.length(); i++)
	{
		if ((int)kod[i]+klucz > 122)
		{
			pom = (int)kod[i] + klucz - 126;
			kod[i] = (char)(97 + pom);
		}
		if ((int)kod[i]+klucz <= 122)
		{
			kod[i] += klucz;
		}
	}
	return kod;
}

string odkodString(string kod, int klucz)
{
    int pom;
	for (int i = 0; i < kod.length(); i++)
	{
		if ((int)kod[i]-klucz <97)
		{
			pom = 99 -(int)kod[i] - klucz;
			kod[i] = (char)(122 - pom);
		}
		if ((int)kod[i]+klucz >= 97)
		{
			kod[i] -= klucz;
		}

	}
	return kod;
}

int main()
{

	int klucz = 3;
	string kod = "allelujlazzzza";
	string zakodowanaWiadomosc = kodCezara(kod, klucz);
	cout<<kod<<"\n";
	cout <<odkodString(zakodowanaWiadomosc, klucz);

}

//65 - 90
