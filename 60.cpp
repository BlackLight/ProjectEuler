#include <iostream>
#include <sstream>
#include <vector>
#include <map>
#include <cstdlib>
#include <sys/types.h>
using namespace std;

#define	SIZE		5
#define 	MAXPRIME 	10000

vector<int> primes;
map<int,int> hash;

bool MillerRabin(unsigned long long int n, unsigned long long int k)  {
	if(n == k) return true;
	unsigned long long int s, d, b, e, x;
   
	for(s = 0, d = n - 1; !(d & 1); s++)
		d >>= 1;

	for(x = 1, b = k % n, e = d; e; e >>= 1)  {
		if(e & 1) x = (x * b) % n;
		b = (b * b) % n;
	}
   
	if(x == 1 || x == n-1) return true;

	while(s-- > 1)  {
		x = (x * x) % n;
		if(x == 1) return false;
		if(x == n-1) return true;
	}
	
	return false;
}

bool isPrime(int n)  {
	return (n>73&&!(n%2&&n%3&&n%5&&n%7&&
		n%11&&n%13&&n%17&&n%19&&n%23&&n%29&&
		n%31&&n%37&&n%41&&n%43&&n%47&&n%53&&
		n%59&&n%61&&n%67&&n%71&&n%73))?false:
		MillerRabin(n, 2)&&MillerRabin(n, 7)
		&&MillerRabin(n, 61);
}

bool isOrdered (vector<int> v)  {
	for (int i=0; i < v.size()-1; i++)
		if (v[i] > v[i+1])
			return false;

	return true;
}

vector<int> genPrimes (int maxPrime)  {
	vector<int> primes;

	for (int i=2; i <= maxPrime; i++)  {
		if (isPrime(i))  {
			hash[i] = primes.size();
			primes.push_back(i);
		}
	}

	return primes;
}

int nextPrime (int n)  {
	if (n < MAXPRIME)
		if (primes[hash[n]+1] > 0)
			return primes[hash[n]+1];

	for (n=n+1; !isPrime(n); n++);
	return n;
}

int concat (int a, int b)  {
	int res;
	stringstream ss;
	ss << a << b;
	ss >> res;
	return res;
}

bool isSeqOk (vector<int> seq)  {
	if (!isOrdered(seq))
		return false;

	for (int i=0; i < seq.size(); i++)  {
		for (int j=0; j < seq.size(); j++)  {
			if (i != j)  {
				int val = concat(seq[i], seq[j]);

				if (!hash.count(val))  {
					if (!isPrime(val))
						return false;
				}
			}
		}
	}

	return true;
}

bool genPrimeSeq (int minVal, int maxVal, vector<int>& seq)  {
	bool allMax = true;

	for (int i=0; i < seq.size() && allMax; i++)  {
		if (seq[i] < maxVal)
			allMax = false;
	}

	if (allMax)
		return false;

	int index = seq.size() - 1;

	for (; index >= 0 && seq[index] >= maxVal; index--);
	seq[index] = nextPrime(seq[index]);

	if (index == 0)
		cout << seq[index] << endl;

	if (index != seq.size() - 1)  {
		for (int i = seq.size()-1; i > index; i--)
			seq[i] = minVal;
	}
	
	return true;
}

int main (int argc, char **argv)  {
	cout << "Generating primes...\n";
	primes = genPrimes(10000000);
	cout << "done!\n";
	vector<int> v;

	for (int i=0; i < SIZE; i++)
		v.push_back(2);

	do  {
		if (isSeqOk(v))  {
			int sum = 0;

			for (int i=0; i < SIZE; i++)  {
				cout << v[i] << ", ";
				sum += v[i];
			}

			cout << endl << sum << endl;
			return 0;
		}
	} while (genPrimeSeq(2, MAXPRIME, v));

	return 0;
}

