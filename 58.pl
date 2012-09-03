#!/usr/bin/perl

use strict;
use warnings;

sub prime  {
	my $num = shift;

	return 0 if ($num<1);
	return 1 if ($num==2);
	return 1 if ($num==3);
	return 0 if (!($num%2));

	for (my $i=3; $i<=$num/2; $i+=2)  {
		return 0 if (!($num%$i));
	}

	return 1;
}

sub num_primes  {
	my $size = shift;

	return -1 if (!($size%2));
	return  0 if ($size==1);

	my $start = ($size-2)*($size-2) + 1;
	my $end = $size*$size;
	my $count = 0;

	for (my $i=$start; $i<=$end; $i += ($size-2))  {
		if (prime($i) && ($i ne $start))  {
			$count++;
		}

		$i++ if ($i!=$start);
	}

	return $count;
}

my $cur=3;
my $primes=0;
my $diag=1;
my $ratio=100;

for (my $i=3; $ratio>10; $i+=2)  {
	for (my $j=$cur; $j<=$i; $j+=2)  {
		$primes += num_primes($j);
		$diag += 4;
	}

	my $ratio = (($primes/$diag)*100);
	print "$i: $ratio\n";
	$cur=$i+2;
}

