#include <iostream>
using namespace std;

int funkcja(int i)
{
	for (int g=2;g<i;g++)
	{
		if (i%g==0)
		{
			cout<<"To nie jest liczba pierwsza";
			return 0;
		}
	}
	cout<<"To jest liczba pierwsza";
}

int main()
{
	int i;
	cin>>i;
	int f = funkcja(i);
}
