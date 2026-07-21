#include <iostream>
using namespace std;
void fi()
{
	int a;
	cin >> a;
	int b = 0;
	int c = 1;
	for (int i = 0; i <= a; i++)
	{
		cout << b << " ";
		c += b;
		b = c - b;
	}
}
int main()
{
	fi();
	return 0;
}