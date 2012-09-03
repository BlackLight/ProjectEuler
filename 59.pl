#!/usr/bin/perl

use strict;
use warnings;

open IN, '< cipher1.txt';
my $row = <IN>;
close IN;

my @file = split /,/, $row;

foreach my $key ('aaa'..'zzz')  {
	my @k = split //, $key;
	my @cif;
	
	for (my $i=0; $i < int(@file); $i++)  {
		push @cif, chr( int($file[$i]) ^ ord($k[$i % int(@k)]) );
	}

	my $plain = join '', @cif;

	if ($plain =~ /^[a-zA-Z0-9\s\\.\,\:\;\(\)\!\?\'\"]+$/)  {
		print $plain."\n\n";

		for (my $i=0; $i < int(@cif); $i++)  {
			$cif[$i] = ord($cif[$i]);
		}

		my $sum = 0;

		foreach my $num (@cif)  {
			$sum += $num;
		}

		print " --> Somma: $sum\n";
		exit;
	}
}

