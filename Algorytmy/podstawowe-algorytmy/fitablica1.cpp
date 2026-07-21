#include <iostream>
using namespace std;
void ciagfi()
{
	int a[100000];
	a[0]=0;
	a[1]=1;
	int b;
	cin>>b;
	for (int i=2; i<=b; i++)
	{
		a[i]=a[i-1]+a[i-2];
	}
	cout<<a[b];
}
int main()
{
	ciagfi();
	return 0;
}
