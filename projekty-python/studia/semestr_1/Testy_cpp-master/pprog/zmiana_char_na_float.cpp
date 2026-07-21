#include <cstdlib>
#include <iostream>
#include <string>
using namespace std;

string* funkcja(string** tab, int g, int n) {

    string* tab2 = new string[n];
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < g; j++)
        {
            tab2[i].append(tab[j][i]);
            cout <<" "<< tab2[i][j];
        }
        cout << endl;
    }
    return tab2;
}

int main() {
    int g = 2;
    int n = 5;
    cin >> g >> n;
    string** tab = new string* [n];
    for (int i = 0; i < n; ++i)
    {
        tab[i] = new string[g];
        for (int j = 0; j < g; j++)
        {
            tab[i][j] = rand();
            cout << tab[i][j] << " ";
        }
        cout << endl;
    }
    cout << endl;
    string* cos = funkcja(tab, n, g);
    return 0;
}