#include <iostream>
using namespace std;

int funkcja (int i, int g)
{
	while(i!=g)
	{
		if (i>g)
		{
			i-=g;
		}
		if (g>i)
		{
			g-=i;
		}
	}
	cout<<g;
	return 0;
}

int main()
{
	int g, i;
	cin>>g>>i;
	int nwd = funkcja(i,g);
}
