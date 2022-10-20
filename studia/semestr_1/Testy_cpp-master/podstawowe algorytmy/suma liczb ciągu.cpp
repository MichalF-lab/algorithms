#include <iostream>
using namespace std;

int funkcja(int a, int b)
{
	int sumaliczb = 0;
	while(b--)
	{
		sumaliczb+=a;
		a++;
	}
	cout<<sumaliczb;
	return 0;
}

int main()
{
	int a,b;
	cout<<"POdaj liczbe startow¹ a nastêpnie ile licz ma byæ zsumowanych"<<endl;
	cin>>a>>b;
	int suma = funkcja(a,b); 
}
