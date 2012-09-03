#include <stdio.h>

int ABS (int x)  {
	if (x<0) return -x;
	else return x;
}

main()  {
	int a,b;
	int i,j;
	int count=0;
	int rect=0;
	int round=100;
	int limit = 2000000;

	for (a=2; ; a++)  {
		for (b=1; ; b++)  {
			count=0;

			for (i=0; i<a; i++)
				for (j=0; j<b; j++)
					count += (a-i)*(b-j);

			rect=count;
			
			if (ABS(limit-rect) <= round)  {
				printf ("%d*%d = %d => %d rect",a, b, a*b, rect);
				getchar();
				round = ABS(rect-limit);
			}

			if (rect>2000016)
				break;
		}
	}
}

