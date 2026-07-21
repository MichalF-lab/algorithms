class liczba{
    int wartosc;
    void zapisz(int ile);

    void zapisuje_sb();
};

void liczba::zapisz(int ile){
    wartosc = ile;
}
void liczba::zapisz(int ile){
    this->wartosc = ile;
}
// to to samo !
// this nie może być modyfikowane ani nie ma swgo adresu

//---------------------------------------------

void zapisy(const liczba* ta);
// Należy dodać const ale jego brak nie będzie błedem

void liczba::zapisuje_sb(){
    zapisy(this);
}

//---------------------------------------------

class ile_ocen{
public:
    static int lacznie;
    // Wspólny

    void dodaj(int ile){
        lacznie+=ile;
    }
};

int ile_ocen::lacznie = 6;


int main_1(){
    ile_ocen nasza_klasa;
    ile_ocen nasza_klasa_2;
    nasza_klasa.dodaj(3);
    //cout << nasza_klasa_2.lacznie; da wynik 9
}

//---------------------------------------------

#include <iostream>
#include <string>
#include <vector>

using namespace std;

inline void to() {
	int a;
}

class Tklasa {
public:
	string imie{ "nieznane imie" };
	double* wskaznik{ nullptr };
	int  tablicaA[5]{ 100, 200, 300 };
	vector<char> symbole{ 'a','b','c' };
	enum stan { pauza = 40, stop = 55, play = 66, przewijanie = 77 };
	stan  odtwarzacz{ stop };
};

void f(int* tab) {
	tab[0] = 13;
}

void fo(int tab[5]) {
	tab[0] = 133;
}


class ile_ocen {
public:
	static int lacznie;
	void dodaj(int ile) {
		lacznie += ile;
	}
};

int ile_ocen::lacznie = 6;


int main() {
	Tklasa ob; cout << "Wstepna zawartosc kazdego nowego obiektu klasy Tklasa to:\n"
		<< "ob.imie= " << ob.imie
		<< ", ob.wskaznik = " << ob.wskaznik
		<< ", odtwarzacz jest w stanie = " << ob.odtwarzacz
		<< endl
		; cout << "Tresc tablicyA: ";
	for (int k : ob.tablicaA) cout << k << ", ";

	cout << "Tresc wektora symbole: ";
	for (auto s : ob.symbole) cout << s << ", ";

	const  double obiekt_staly = 15.6;
	double   obiekt_zwykly;
	obiekt_zwykly = obiekt_staly;

	int* to = new int[12];
	//f(to);
	fo(to);
	cout << "\n" << to[0]<<"\n";


	ile_ocen nasza_klasa;
	ile_ocen nasza_klasa_2;

	

	nasza_klasa.dodaj(3);

	cout << nasza_klasa_2.lacznie;

}