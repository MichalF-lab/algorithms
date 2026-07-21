#include <cstdlib>
#include <iostream>
using namespace std;

bool** funkcja(float** tab1,float** tab2, int n, int m) {
    bool** tab = new bool* [n];
    for (int i = 0; i < n; ++i) tab[i] = new bool[m];
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < m; j++)
        {
            if (tab1[i][j]==tab2[i][j]) tab[i][j]=true;
            else tab[i][j]=false;
            cout<<tab[i][j]<<" ";
        }
        cout << endl;
    }
    return tab;
}

int main() {
    int n = 4;
    int m = 3;
    float** tab1 = new float* [n];
    for (int i = 0; i < n; ++i)
    {
        tab1[i] = new float[m];
        for (int j = 0; j < m; j++)
        {
            tab1[i][j] = rand();
            cout << tab1[i][j] << " ";
        }
        cout << endl;
    }
    cout << endl;
    float** tab2 = new float* [n];
    for (int i = 0; i < n; ++i)
    {
        tab2[i] = new float[m];
        for (int j = 0; j < m; j++)
        {
            tab2[i][j] = rand();
            cout << tab2[i][j] << " ";
        }
        cout << endl;
    }
    cout << endl;
    tab1[1][1]=tab2[1][1];
    tab1[4][3]=tab2[4][3];
    bool** cos = funkcja(tab1, tab2, n, m);
    return 0;
}