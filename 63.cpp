#include <iostream>
#include <NTL/ZZ.h>

NTL_CLIENT

int ndigit (ZZ n)  {
	return (int) (log(n) / log(to_ZZ(10))) + 1;
}

main()  {
	int count=0;

	for (int exp=1; exp<100; exp++)  {
		for (ZZ i=to_ZZ(1); i<100; i++)  {
			ZZ p = power(i,exp);

			if ( (ndigit(p) == exp) && (i%10) )
				count++;
		}
	}

	cout << "** count -> " << count << endl;
}

