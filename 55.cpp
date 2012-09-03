#include <iostream>
#include <NTL/ZZ.h>

NTL_CLIENT

unsigned int ndigits (ZZ a)  {
	return (unsigned long) (log(a)/log(to_ZZ(10)))+1;
}

string toString (ZZ a)  {
	int n = ndigits(a);
	string s;

	for (int i=0; a > to_ZZ(0); i++)  {
		long int cif = to_long(a / power(to_ZZ(10), n-i-1));
		a -= (cif*power(to_ZZ(10), n-i-1));
		s += (cif+'0');
	}

	return s;
}

ZZ to_ZZ (string s)  {
	int n = s.size();
	ZZ  a = to_ZZ(0);

	for (int i=0; i<n; i++)
		a += (s[i]-'0')*power(to_ZZ(10), n-i-1);
	return a;
}

string reverse (string s)  {
	string r;

	for (int i=0; i<s.size(); i++)
		r += s[s.size()-i-1];
	return r;
}

bool palindrome (ZZ a)  {
	string s = toString(a);
	return !(s.compare( reverse(s) ));
}

bool is_lychrel (ZZ a)  {
	bool lychrel=false;
	a += to_ZZ(reverse(toString(a)));

	for (int i=0; i<50 && !lychrel; i++)  {
		if (palindrome(a))  {
			lychrel=true;
			return lychrel;
		} else {
			a += to_ZZ(reverse(toString(a)));
		}
	}

	return lychrel;
}

main()  {
	int count=0;

	for (int i=1; i<10000; i++)  {
		if (!is_lychrel(to_ZZ(i)))
			count++;
	}

	cout << count << endl;
}

