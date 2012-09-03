#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

typedef unsigned long long int ll;

int reverse (int n)  {
	int i,rev,digits = (int) log10f(n)+1;
	char *s1 = (char*) malloc(digits);
	char *s2 = (char*) malloc(digits);

	sprintf (s1,"%llu",n);

	for (i=0; i<strlen(s1); i++)
		s2[i] = s1[strlen(s1)-i-1];
	s2[i]=0;
	rev=atoi(s2);

	free(s1);
	free(s2);
	return rev;
}

int palindromic (int n)  {
	int i;
	char s1[100];
	char s2[100];

	sprintf (s1,"%d",n);

	for (i=0; i<strlen(s1); i++)
		s2[i] = s1[strlen(s1)-i-1];
	s2[i]=0;

	if (!strcmp(s1,s2))
		return 1;
	else
		return 0;
}

main()  {
	int i, steps, ok, tmp, count=0;
	const int limit=90;

	for (i=10; i<limit; i++)  {
		for (
				ok=0, tmp=i;
				!ok && tmp < (int) pow(2,32)-1;
				steps++
			)  {

			if (palindromic(tmp + reverse(tmp)))  {
				ok=1;
			}
			else  {
				tmp += reverse(tmp);
				
				if (i==89)
					printf ("%d\n",tmp);
			}
		}

		if (!ok)
			count++;
	}

	printf ("count: %d\n",count);
}

