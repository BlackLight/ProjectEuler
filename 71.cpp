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
	quad_float val = to_quad_float(3.0/7.0);
	quad_float prec = to_quad_float(0.0);
	fract my_f;
	
	for (int i=999900; i<=1000000; i++)  {
		for (int j=1; j<i; j++)  {
			fract f;
			f.num=j;
			f.den=i;

			if (
					( (to_quad_float(to_quad_float(j) / to_quad_float(i))) >= prec) &&
					( (to_quad_float(to_quad_float(j) / to_quad_float(i))) < val ) &&
					(j!=3) && (i!=7)
			   )  {
				if (!cfactor(f))  {
					my_f = f;
					prec = to_quad_float(to_quad_float(j) / to_quad_float(i));
				}
			}
		}
	}

	cout << my_f.num << "/" << my_f.den << endl;
}

