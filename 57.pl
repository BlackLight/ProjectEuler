#!/usr/bin/perl

use strict;
use warnings;

my $expr = '1+(1/2)';
my $count=0;

foreach my $i (0..999)  {
	my $res = sprintf("%.100f",eval($expr));

	#print "$expr = $res\n";

	foreach my $j (1..1000)  {
		if (($res*$j) =~ /^([0-9]+)$/)  {
			if (length($1) > (length($j)))  {
				$count++;
				print "   => $1/$j\n";
			}

			last;
		}
	}

	$expr =~ s/1\/2/1\/\(2+1\/2\)/;
	print "$res\n";
}

print $count."\n";

