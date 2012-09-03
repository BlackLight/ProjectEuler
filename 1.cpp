#include <iostream>
#include <vector>
#include <cmath>
using namespace std;

bool is_prime (int n)  {
        int i,limit = (int) sqrt(n)+1;

        if (n<0) return false;
        if ((n==2) || (n==3) || (n==5) || (n==7)) return true;
        if (!(n%2)) return false;

        for (i=3; i<limit; i+=2)
                if (!(n%i)) return false;
        return true;
}

vector<int> get_factors (int n)  {
	vector<int> fact;

	while (n>1)  {
		for (int i=2; i<=n && n>1; i++)  {
			if ( (is_prime(i)) && (!(n%i)) )  {
				bool found=false;

				for (int j=0; j<fact.size(); j++)  {
					if ( (fact[j] == i) || (!(fact[j]%i)) )  {
						found=true;
						fact[j]*=i;
					}
				}

				if (!found)
					fact.push_back(i);
				n /= i;
			}
		}
	}

	return fact;
}

main()  {
	const int from  = 342055;
	const int limit = 400000;

	for (int i=from; i<limit; i++)  {
		if (!is_prime(i) && !is_prime(i+1) && !is_prime(i+2))  {
			vector<int> v1 = get_factors(i);
			vector<int> v2 = get_factors(i+1);
			vector<int> v3 = get_factors(i+2);
			vector<int> v4 = get_factors(i+3);
			bool common = false;

			if (v1.size()==4)
				cout << i << endl;

			if ((v1.size()!=v2.size()) ||
					(v2.size()!=v3.size()) ||
					(v3.size()!=v4.size()) ||
					(v1.size()!=4))
				common=true;

			else  {
				for (int j=0; j<v1.size(); j++)  {
					if (binary_search(v2.begin(), v2.end(), v1[i]) ||
							binary_search(v3.begin(), v3.end(), v1[i]) ||
							binary_search(v4.begin(), v4.end(), v1[i]))  {
						common=true;
						break;
					}
				}
			}

			out:
			if (!common)  {
				cout << i << endl;
				break;
			}
		}
	}
}

