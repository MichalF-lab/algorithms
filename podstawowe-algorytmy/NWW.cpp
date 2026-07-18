#include <iostream>
using namespace std;

int funkcja(int a, int b)
{
	int c=a,d=b;
	while(a!=b)
	{
		if(a>b) b+=d;
		if(b>a) a+=c;
	}
	cout<<a;
	return 0;
}

int main()
{
	int a,b;
	cin>>a>>b;
	int f = funkcja (a,b);
}
