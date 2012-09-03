#include <iostream>
#include <sstream>
#include <string>
#include <algorithm>
#include <vector>
#include <map>
using namespace std;

#define 	MINCUBE 	7060
#define 	MAXCUBE 	7062
#define 	PERMS 	5

typedef unsigned long int      uint32;
typedef unsigned long long int uint64;

map<uint64, uint32> hash;

vector<int> split (uint64 n)  {
	vector<int> v;
	stringstream ss;
	ss << n;
	string::iterator it;

	for (it = ss.str().begin(); it != ss.str().end() && *it >= '0' && *it <= '9'; it++)  {
		if (*it >= '0' && *it <= '9')
			v.push_back(*it - '0');
	}

	return v;
}

uint64 join (vector<int> v)  {
	uint64 n;
	stringstream ss;

	for (int i=0; i < v.size(); i++)
		ss << v[i];
	ss >> n;
	return n;
}

int countPerms (uint64 n)  {
	int count = 0;
	vector<int> digits = split(n);
		
	do  {
		if (hash.count(join(digits)) > 0)
			count++;
	} while (next_permutation(digits.begin(), digits.end()));

	return count;
}

int main()  {
	cout << "Generating cubes...\n";
	for (int i=MINCUBE; i < MAXCUBE; i++)
		hash[i*i*i] = i;
	cout << "done!\n";

	map<uint64, uint32>::iterator it;

	for (it = hash.begin(); it != hash.end(); it++)  {
		if (!(it->second % 100))
			cout << "... " << it->second << endl;

		if (countPerms(it->first) == PERMS)  {
			cout << it->first << " -> " << it->second << endl;
			return 0;
		}
	}

	return 1;
}

