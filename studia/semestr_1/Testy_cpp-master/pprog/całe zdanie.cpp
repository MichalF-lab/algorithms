#include <string>
#include <iostream>

using namespace std;

struct Adres
{
    string miasto;
    string ulica;
    int nr_domu;
    int nr_mieszkania;
    int kod;
};


struct Osoba
{
    string* imie;
    int ile_imion;
    string nazwisko;
    Adres adres;
    int ID_klienta;
};

struct Autor
{
    string* imie;
    int ile_imion;
    string nazwisko;
    int ID_autora;
};


struct Book
{
    string tytul;
    Autor autor;
    string ISBN;
    string wydawnictwo;
    int rok_wydania;
    string seria_wydawnicza;
    // jako ze moze byc pare takich samych ksiazek nalezy dodac klucz glówny
    int ID_ksiazek;
};


int f_ID_autora(Autor nowy, Autor* tablica_autorow, int ile_autorow, int& ID_autora) {
    if (tablica_autorow == nullptr) return 0;
    for (int i = 0; i < ile_autorow; i++) {
        if (tablica_autorow[i].imie == nowy.imie) {
            if (tablica_autorow[i].nazwisko == nowy.nazwisko) return tablica_autorow[i].ID_autora;
        }
    }
    ID_autora++;
    return ID_autora;
}


Autor create_autor(string* imie, int ile_imion, string nazwisko, int& ID_autora, Autor* tablica_autorow, int ile_autorow) {
    Autor autor = { imie,ile_imion, nazwisko, ID_autora };
    autor.ID_autora = f_ID_autora(autor, tablica_autorow, ile_autorow, ID_autora);
    return autor;
}

void f(int* y, int x) {
    *y = x;
}

void add_autor(string* imie, int ile_imion, string nazwisko, int& ID_autora, Autor** tablica_autorow, int& ile_autorow) {
    Autor* tablica_autorow_pom = new Autor[++ile_autorow];
    if (*tablica_autorow != nullptr) {
        for (int i = 0; i <= ile_autorow; i++) {
            tablica_autorow_pom[i] = (*tablica_autorow)[i];
        }
        delete[] * tablica_autorow;
    }
    tablica_autorow_pom[ile_autorow - 1] = create_autor(imie, ile_imion, nazwisko, ID_autora, *tablica_autorow, ile_autorow);

    *tablica_autorow = tablica_autorow_pom;
}

void print_autor(Autor autor) {
    for (int i = 0; i < autor.ile_imion; i++) cout << autor.imie[i] << " ";
    cout << autor.nazwisko << " " << autor.ID_autora << endl;
}



Book create_book(string tytul, Autor autor, string ISBN, string wydawnictwo, int rok_wydania, string seria_wydawnicza, int& Id_ksiazek) {
    Book ksiazka = { tytul, autor, ISBN, wydawnictwo, rok_wydania, seria_wydawnicza, Id_ksiazek };
    Id_ksiazek++;
    return ksiazka;
}

void add_book(string tytul, Autor autor, string ISBN, string wydawnictwo, int rok_wydania, string seria_wydawnicza, Book** tablica_ksiazek, Book* const_tab_ksiazek, int& ile_ksiazek, int& Id_ksiazek, bool** tablica_ksiazek_wypozyczonych, bool* const_tab_wypozyczonych) {
    Book* tablica_ksiazek_pom = new Book[++ile_ksiazek];
    bool* tablica_ksiazek_wypozyczonych_pom = new bool[ile_ksiazek];
    if (*tablica_ksiazek != nullptr) {
        for (int i = 0; i < ile_ksiazek - 1; i++) {
            tablica_ksiazek_pom[i] = const_tab_ksiazek[i];
            tablica_ksiazek_wypozyczonych_pom[i] = const_tab_wypozyczonych[i];
        }
        delete[] * tablica_ksiazek;
        delete[] * tablica_ksiazek_wypozyczonych;
    }

    tablica_ksiazek_pom[ile_ksiazek - 1] = create_book(tytul, autor, ISBN, wydawnictwo, rok_wydania, seria_wydawnicza, Id_ksiazek);
    tablica_ksiazek_wypozyczonych_pom[ile_ksiazek - 1] = false;

    *tablica_ksiazek = tablica_ksiazek_pom;
    *tablica_ksiazek_wypozyczonych = tablica_ksiazek_wypozyczonych_pom;
}

void delete_book(Book ksiazka, Book** tablica_ksiazek, int& ile_ksiazek, bool** tablica_ksiazek_wypozyczonych) {
    if (*tablica_ksiazek != nullptr) {
        for (int i = 0; i < ile_ksiazek; i++) {
            if ((*tablica_ksiazek)[i].ID_ksiazek == ksiazka.ID_ksiazek) {
                Book* tablica_ksiazek_pom = new Book[--ile_ksiazek];
                bool* tablica_ksiazek_wypozyczonych_pom = new bool[ile_ksiazek];
                Book* adres_1 = tablica_ksiazek_pom;
                bool* adres_2 = tablica_ksiazek_wypozyczonych_pom;
                for (int j = 0; j <= ile_ksiazek; j++) {
                    if (i == j) {
                        ++j;
                    }
                    *tablica_ksiazek_pom = (*tablica_ksiazek)[j];
                    *tablica_ksiazek_wypozyczonych_pom = (*tablica_ksiazek_wypozyczonych)[j];
                    tablica_ksiazek_pom++;
                    tablica_ksiazek_wypozyczonych_pom++;
                }


                delete[](*tablica_ksiazek);
                delete[](*tablica_ksiazek_wypozyczonych);
                (*tablica_ksiazek) = adres_1;
                (*tablica_ksiazek_wypozyczonych) = adres_2;
                cout << (*tablica_ksiazek_wypozyczonych) << endl;
                cout << "Pomyslnie usunieto ksiazke" << endl;
                return;
            }
        }
        cout << "Nie znaleziono takiej ksiazki " << endl;
    }
    cout << "tablica ksiazek jest pusta";
}

Osoba create_person(string* imie, int ile_imion, string nazwisko, Adres adres, int& ID_klienta) {
    Osoba klient = { imie, ile_imion, nazwisko, adres, ID_klienta };
    ID_klienta++;
    return klient;
}

void add_person(string* imie, int ile_imion, string nazwisko, Adres adres, int& ID_klienta, int& ile_klientow, Osoba** tablica_kilentow) {
    if (*tablica_kilentow != nullptr) {
        Osoba* tablica_klientow_pom = new Osoba[++ile_klientow];
        for (int i = 0; i < ile_klientow; i++) tablica_klientow_pom[i] = (*tablica_kilentow)[i];
        tablica_klientow_pom[ile_klientow - 1] = create_person(imie, ile_imion, nazwisko, adres, ID_klienta);
        delete[] * tablica_kilentow;
        (*tablica_kilentow) = tablica_klientow_pom;
    }
    else {
        Osoba* tablica_klientow_pom = new Osoba[++ile_klientow];
        *tablica_klientow_pom = create_person(imie, ile_imion, nazwisko, adres, ID_klienta);
        (*tablica_kilentow) = tablica_klientow_pom;
    }
}



Book* find_by_autor(Book* tablica_ksiazek, int ile_ksiazek, Autor autor) {
    int pom1 = 0;
    for (int i = 0; i < ile_ksiazek; i++) {
        if (tablica_ksiazek[i].autor.ID_autora == autor.ID_autora)  pom1++;
    }
    Book* print = new Book[pom1];
    for (int i = 0; i < ile_ksiazek; i++) {
        if (tablica_ksiazek[i].autor.ID_autora == autor.ID_autora) print[--pom1] = tablica_ksiazek[i];
    }
    return print;
}

Book find_by_title(string title, int ile_ksiazek, Book* tablica_ksiazek) {
    for (int i = 0; i <= ile_ksiazek; i++) if (tablica_ksiazek[i].tytul == title) return tablica_ksiazek[i];
}

Book* find_by_print(string wydawnictwo, int ile_ksiazek, Book* tablica_ksiazek) {
    int pom = 0;
    for (int i = 0; i <= ile_ksiazek; i++) {
        if (tablica_ksiazek[i].seria_wydawnicza == wydawnictwo)  pom++;
    }
    if (pom == 0) cout << "Nie znalezlismy zadnych pasujacych wynikow " << endl;
    else
    {
        Book* print = new Book[pom];
        for (int i = 0; i <= ile_ksiazek; i++) {
            if (tablica_ksiazek[i].seria_wydawnicza == wydawnictwo) {
                *print = tablica_ksiazek[i];
                print++;
            }
        }
        return print;
    }
}



void wypozycz(Book ksiazka, Book* tablica_ksiazek, bool** tablica_ksiazek_wypozyczonych, int ile_ksiazek) {
    for (int i = 0; i < ile_ksiazek; i++) {
        if (ksiazka.ID_ksiazek == tablica_ksiazek[i].ID_ksiazek) {
            if (*tablica_ksiazek_wypozyczonych[i] != true) {
                *tablica_ksiazek_wypozyczonych[i] = true;
                cout << "Wypozyczono pomyslnie " << endl;
                return;
            }
            else {
                cout << "Ksiazka zostala juz wyporzyczona " << endl;
                return;
            }
        }
    }
    cout << "Nie znalezlismy takiej ksiazki " << endl;
}

void zwroc(Book ksiazka, Book* tablica_ksiazek, bool** tablica_ksiazek_wypozyczonych, int ile_ksiazek) {
    for (int i = 0; i < ile_ksiazek; i++) {
        if (ksiazka.ID_ksiazek == tablica_ksiazek[i].ID_ksiazek) {
            if ((*tablica_ksiazek_wypozyczonych)[i] == true) {
                *tablica_ksiazek_wypozyczonych[i] = false;
                cout << "Zwrocono pomyslnie " << endl;
                return;
            }
            else {
                cout << "Ksiazka nie zostala wypozyczona " << endl;
                return;
            }
        }
    }
    cout << "Nie znalezlismy takiej ksiazki " << endl;
}



int main(void) {
    int y = 5;
    f(&y, 3);

    int ID_autora = 0, ile_autorow = 0, Id_ksiazek = 0, ile_ksiazek = 0, ID_klienta = 0, ile_klientow = 0;

    Book* tablica_ksiazek = nullptr;
    Osoba* tablica_kilentow = nullptr;
    Autor* tablica_autorow = nullptr;
    bool* tablica_ksiazek_wypozyczonych = nullptr;

    string* imiona = new string[2];
    imiona[0] = "Maciej";
    imiona[1] = "Tomasz";

    add_autor(imiona, 2, "Sapkowski", ID_autora, &tablica_autorow, ile_autorow);

    print_autor(tablica_autorow[0]);

    add_book("Ostatnie Zyczenie", tablica_autorow[0], "1234567890123", "Nowa era", 2003, "Wiedzmin", &tablica_ksiazek, tablica_ksiazek, ile_ksiazek, Id_ksiazek, &tablica_ksiazek_wypozyczonych, tablica_ksiazek_wypozyczonych);
    add_book("Wieza Jaskolki", tablica_autorow[0], "1234567890123", "Nowa era", 1998, "Wiedzmin", &tablica_ksiazek, tablica_ksiazek, ile_ksiazek, Id_ksiazek, &tablica_ksiazek_wypozyczonych, tablica_ksiazek_wypozyczonych);
    add_book("Wieczny Ogien", tablica_autorow[0], "1234567890123", "Nowa era", 1993, "Wiedzmin", &tablica_ksiazek, tablica_ksiazek, ile_ksiazek, Id_ksiazek, &tablica_ksiazek_wypozyczonych, tablica_ksiazek_wypozyczonych);

    delete_book(tablica_ksiazek[1], &tablica_ksiazek, ile_ksiazek, &tablica_ksiazek_wypozyczonych);

    add_book("Wieczny Ogien", tablica_autorow[0], "1234567890123", "Nowa era", 1993, "Wiedzmin", &tablica_ksiazek, tablica_ksiazek, ile_ksiazek, Id_ksiazek, &tablica_ksiazek_wypozyczonych, tablica_ksiazek_wypozyczonych);

    delete_book(tablica_ksiazek[1], &tablica_ksiazek, ile_ksiazek, &tablica_ksiazek_wypozyczonych);

    Adres adres = { "Poznan","Fredry",12,12,12 };

    add_person(imiona, 2, "Jankowiak", adres, ID_klienta, ile_klientow, &tablica_kilentow);

    Book* by_autor = find_by_autor(tablica_ksiazek, ile_ksiazek, tablica_autorow[0]);
    Book by_title = find_by_title("Wieza Jaskolki", ile_ksiazek, tablica_ksiazek);
    Book* by_wydawnictwo = find_by_print("Nowa era", ile_ksiazek, tablica_ksiazek);

    wypozycz(tablica_ksiazek[0], tablica_ksiazek, &tablica_ksiazek_wypozyczonych, ile_ksiazek);
    zwroc(tablica_ksiazek[0], tablica_ksiazek, &tablica_ksiazek_wypozyczonych, ile_ksiazek);
    zwroc(tablica_ksiazek[1], tablica_ksiazek, &tablica_ksiazek_wypozyczonych, ile_ksiazek);

    return 0;
}