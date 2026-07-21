#include <iostream>
using namespace std;
int funkcja (int i)
{	
	do
	{
		cout<<i%10<<"  ";
		i = i/10 ;
	} while (i>1);
	return 0;
}

int main()
{
	int i;
	cin>>i;
	int rozkald = funkcja (i);
}
