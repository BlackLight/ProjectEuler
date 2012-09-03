#!/usr/bin/perl

use strict;
use warnings;

sub contains  {
	my ($val,@array) = @_;

	foreach my $element (@array)  {
		$val =~ /([0-9]+)/;
		my $intval = $1;

		$element =~ /([0-9]+)/;
		my $intel = $1;

		if ($intval && $intel)  {
			return 1 if ($intel == $intval);
		}
	}

	return 0;
}

open IN,'< keylog.txt';
my @file; my @vals;

while (<IN>)  {
	push @file, $_;
}

close IN;

foreach my $el (@file)  {
	push @vals, $el if (!contains($el, @vals));
}

foreach my $el (@vals)  {
	print $el;
}

