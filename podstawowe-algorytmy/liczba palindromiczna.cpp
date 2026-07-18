#include <iostream>
using namespace std;

int funkcja(int i)
{
	int g=i;
	int odwrocona=0;
	while (i>1)
	{
		odwrocona+=i%10;
		if (i>10) odwrocona*=10;
		i/=10;
	}
	if (odwrocona != g)
	{
		cout<<"nie ";
	}
	cout<<" jest palindromiczna";
	return 0;
}

int main()
{
	int i;
	cin>>i;
	int palindromiczna = funkcja(i);
}
