#include <iostream>
using namespace std;
int main()
{
	int i;
	cin>>i;
	for (int h=1; h<=i; h++)
	{
		for (int g=1; g<=h; g++)
		{
			cout<<"O";
		}
		cout<<endl;
	}
	return 0;
}
