#include <iostream>
using namespace std;
int main()
{
	int a,b;
	cin>>a;
	cin>>b;
	for (int i=1; i<=a; i++)
	{
		while (i==1 || i==a)
		{
			for (int o=1; o<=b; o++)
			{
				cout<<"X";
			}
			cout<<endl;
			i++;
		}
		if (i == a+1)
		{
			break;
		}
		cout<<"X";
		for (int z=1; z<=b-2; z++)
		{
			cout<<" ";
		}
		cout<<"X"<<endl;
	}
	return 0;
}
