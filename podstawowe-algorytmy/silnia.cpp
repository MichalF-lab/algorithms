#include <iostream>
using namespace std;

int silnia(int i)
{
	int silnia =1;
	for (int g=1; g<=i;g++)
	{
		silnia*=g;
	}
	cout<<silnia;
	return 0;
}

int main()
{
	int i;
	cin>>i;
	int funkcja = silnia(i);
}
