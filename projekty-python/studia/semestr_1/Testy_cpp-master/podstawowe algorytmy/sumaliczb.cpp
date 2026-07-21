#include <iostream>
using namespace std;

int funkcja(int i)
{
	int suma= 0;
	do
	{
		suma+=i%10;
		i/=10;
	} while (i>1);
	cout<<suma;
	return 0;
}

int main()
{
	int i;
	cin>>i;
	int sumaliczb = funkcja(i);
}
