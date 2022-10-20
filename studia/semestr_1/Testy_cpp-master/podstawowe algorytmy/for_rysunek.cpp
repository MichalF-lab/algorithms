#include <iostream>
using namespace std;

int main()
{
	int i;
	cin >> i;
	for (int h=0; h<=i; h+=2)
	{
		for (int g=0; g<=i*3; g++)
		{
			cout <<"-";
		}	
		cout<<endl;
		for (int g=0; g<=i; g++)
		{
			cout <<"|  ";
		}
		cout<<endl;
	}
	for (int g=0; g<=i*3; g++)
		{
			cout <<"-";
		}	
	return 0;
}
