#include 	<stdio.h>
#include	<stdlib.h>

int main ( int argc, char **argv )  {
	int steps, i, k = 1;
	int *seq;
	int latest_sum = 0;
	int num = 1;
	const int base = 2;

	if (!argv[1])
		return 1;

	steps = atoi(argv[1]);

	if ( steps <= 0 )
		return 1;

	seq = (int*) malloc ( (steps+1) * sizeof(int) );
	seq[0] = base;

	for ( i=1; i <= steps; i++ )  {
		seq[i] = ( ((i-1)%3) == 1 ) ? 2 * (k++) : 1;
		printf (" -> %d\n", seq[i]);
	}

	for ( i=steps; i > 0; i-- )  {
		if ( i < steps )  {
			printf ("num = %d*%d = %d\n", num, seq[i-1], num*seq[i-1]);
			num *= seq[i-1];
			/* printf ("num = %d + (%d*%d) + 1 = %d\\n", num, seq[i], seq[i-1], num + (seq[i] * seq[i-1]) + 1); */
			printf ("num = %d + %d = %d\n", num, latest_sum, num + latest_sum);
			num += latest_sum;
			/* num += (seq[i] * seq[i-1]) + 1; */
		} else {
			printf ("num = (%d*%d) + 1 = %d\n", seq[i], seq[i-1], (seq[i] * seq[i-1]) + 1);
			num = (seq[i] * seq[i-1]) + 1;
			latest_sum = seq[i];
		}
	}

	printf ("%d\n", num);
	free(seq);
	return 0;
}

