#include <iostream>
#include <vector>
#include <algorithm>
#include <NTL/ZZ.h>
#include <NTL/RR.h>

NTL_CLIENT

vector<int> explode (int n)  {
	int tmp=n;
	vector<int> v;
	int n_digits = 9;

	for (int i=n_digits-1; i>=0; i--)  {
		int d = (int) (tmp / powf(10,i));
		v.push_back(d);
		tmp -= (int) (d*powf(10,i));
	}

	return v;
}

ZZ implode (vector<int> v)  {
	ZZ z = to_ZZ(0);

	for (int i=0; i<v.size(); i++)
		z += to_ZZ(v[i]*power(to_ZZ(10), v.size()-i-1));

	return z;
}

main()  {
	vector<int> v1;

	for (int i=0; i<10; i++)
		v1.push_back((i+1)%10);
	
	for (int n = 100000000; n<1000000000; n++)  {
		vector<int> v;
		vector<int> v2 = explode(n);

		for (int i=0; i < v2.size(); i++)  {
			v.push_back(v1[i]);
			v.push_back(v2[i]);
		}

		v.push_back(0);
		ZZ num = implode(v);
		ZZ zz_root = SqrRoot(num);

		if ((zz_root * zz_root) == num)  {
			cout << zz_root << ": " << num << endl;
			break;
		}
	}
}

