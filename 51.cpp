#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>
using namespace std;

bool prime (int n)  {
	if (n<=1) return false;
	if (n==2) return true;
	if (n==3) return true;
	if (!(n%2)) return false;

	for (int i=3; i <= (int) n/2; i+=2)
		if (!(n%i)) return false;

	return true;
}

vector<int> explode (int n)  {
	int tmp=n;
	vector<int> v;
	int n_digits = log10f(n)+1;

	for (int i=n_digits-1; i>=0; i--)  {
		int d = (int) (tmp / powf(10,i));
		v.push_back(d);
		tmp -= (int) (d*powf(10,i));
	}

	return v;
}

int implode (vector<int> v)  {
	int z = 0;

	for (int i=0; i<v.size(); i++)
		z += v[i] * powf(10, v.size()-i-1);
	return z;
}

int main()  {
	for (int i=100; i<999; i++)  {
		vector<int> v = explode(i);

		for (int j=0; j<3; j++)  {
			v[j] = 1;

			if ( prime(implode(v)) )  {
				int count=1;

				for (int k=2; k<10; k++)  {
					if (prime(implode(v)))
						count++;
				}

				if (count==6)  {
					cout << i << endl;
					return 0;
				}
			}
		}
	}
}

