#include <string>
#include <iostream>

using namespace std;

int ID = 0,ile_ksiazek=0;

struct Autor
{
    string* imie;
    int ile_imion;
    string nazwisko;
    int ID;
} Sapkowski;


struct Book
{
    string tytul;
    Autor autor;
    char* ISBN;
    string wydawnictwo;
    int rok_wydania;
    string seria_wydawnicza;
};

Book *tablica = new Book[1000];

int ID_autora (Autor nowy){
    for(int i=0; i<ile_ksiazek;i++){
        if (tablica[i].autor.imie == nowy.imie){
            if (tablica[i].autor.nazwisko == nowy.nazwisko){
                return tablica[i].autor.ID;
            }
        }
    }
    ID++;
    return ID;   
}

Book create_Book() {
    string tytul;
    cout << "Podaj nazwe ksiazki ";
    cin >> tytul;
    int ile_imion;
    cout << endl << "Ile autor ma imion? ";
    cin >> ile_imion;
    string* imie = new string[ile_imion];
    for (int i = 0; i < ile_imion; i++) {
        cout << "Podaj jego "<<i<<" imie";
        cin >> *imie;
        imie++;
    }
    string nazwisko;
    cout << endl << "Podaj nazwiko autora ";
    cin >> nazwisko;
    char ISBN[13];
    cout << endl << "podaj ISBN ";
    for (int i = 0; i < 13; i++) {
        cin >> ISBN[i];
    }
    string wydawnictwo;
    cout << endl << "Podaj wydawnictwo ";
    cin >> wydawnictwo;
    int rok_wydania;
    cout << endl << "Podaj rok wydania ";
    cin >> rok_wydania;
    int seria;
    cout << endl << "Czy ksiązka ma seriw wydawniczą? (jeśli tak naciśnij 1) ";
    cin >> seria;
    string seria_wydawincza ="";
    if (seria == 1) {
        cout  << endl << "Podaj serie wydawniczą ";
        cin >> seria_wydawincza;
    }
    Autor autor = { imie,ile_imion, nazwisko, ID };
    autor.ID = ID_autora (autor);
    Book ksiazka = { tytul, autor, ISBN, wydawnictwo, rok_wydania, seria_wydawincza };
    return ksiazka;
}

void add_Book(Book nazwa) {
    *tablica = nazwa;
    tablica++;
    ile_ksiazek++;
}

Book *find_by_autor(Autor Autor)
{
    int tab=0;
    for(int i=0; i<=ile_ksiazek;i++){
        if (tablica[i].autor.ID == Autor.ID)  tab++;
    }
    Book *print = new Book [tab];
    for(int i=0; i<=ile_ksiazek;i++){
        if (tablica[i].autor.ID == Autor.ID){
            cout<<tablica[i].tytul<<" ";
            *print = tablica[i];
        }
    }
    return print;
}
Book find_by_title(string title){
    for(int i=0; i<=ile_ksiazek;i++){
        if (tablica[i].tytul == title) return tablica[i];
    }
}

Book *find_by_print(string wydawnictwo){
    int tab=0;
    for(int i=0; i<=ile_ksiazek;i++){
        if (tablica[i].seria_wydawnicza == wydawnictwo)  tab++;
    }
    Book *print = new Book [tab];
    for(int i=0; i<=ile_ksiazek;i++){
        if (tablica[i].seria_wydawnicza == wydawnictwo){
            *print = tablica[i];
            print++;
        }
    }
    return print;
}

int main(void) {
    Book Wiedzmin = create_Book();
    Book maly_ksiaze = create_Book();
    add_Book(Wiedzmin);
    add_Book(maly_ksiaze);
    Book ksiazka1 = find_by_title("wiedzmin");
    Book *ksiazka2 = find_by_print("seria");
    Book *ksiazka3 = find_by_autor(Sapkowski);
    return 0;
}