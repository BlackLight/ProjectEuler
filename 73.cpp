#include <iostream>
#include <NTL/quad_float.h>

NTL_CLIENT

typedef struct  {
	int num;
	int den;
} fract;

int MCD (int a, int b)  {
	while (b)  {
		int t=b;
		b = a%b;
		a=t;
	}

	return a;
}

bool cfactor (fract f)  {
	int a = f.num;
	int b = f.den;

	if (MCD(a,b)==1)
		return false;
	else
		return true;
}

main()  {
	quad_float val1 = to_quad_float(1.0/3.0);
	quad_float val2 = to_quad_float(1.0/2.0);
	int count=0;
	
	for (int i=2; i<=10000; i++)  {
		for (int j=1; j<i; j++)  {
			fract f;
			f.num=j;
			f.den=i;

			if (
					( (to_quad_float(to_quad_float(j) / to_quad_float(i))) > val1) &&
					( (to_quad_float(to_quad_float(j) / to_quad_float(i))) < val2 )
			   )  {
				if (!cfactor(f))
					count++;
			}
		}
	}

	cout << count-1 << endl;
}

