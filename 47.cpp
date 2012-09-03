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

int countfact (int n)  {
	vector<int> v;

	do  {
		if (!(n%2))  {
			if (!binary_search(v.begin(), v.end(), 2))
				v.push_back(2);
			n/=2;
		} else {
			if (prime(n))  {
				if (!binary_search(v.begin(), v.end(), n))
					v.push_back(n);
				n=1;
			} else {
				for (int i=3; i <= (int) n/2; i+=2)  {
					if (!(n%i) && prime(i))  {
						if (!binary_search(v.begin(), v.end(), i))
							v.push_back(i);
						n/=i;
						break;
					}
				}
			}
		}
	} while (n>1);

	return v.size();
}

main()  {
	for (int i=100000; i<999996; i++)
		if (
				(countfact(i)==4) &&
				(countfact(i+1)==4) &&
				(countfact(i+2)==4) &&
				(countfact(i+3)==4)
		   )  {
			cout << i << endl;
			break;
		}
}

