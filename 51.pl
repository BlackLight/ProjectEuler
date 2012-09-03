open IN, "<primes51.txt" or die "Cannot open file: $!";
%primes = map {chomp; split /,/} <IN>;
for $p (sort keys %primes) {
  $dd = $primes{$p}; $c=1; $i=0;
  for $d ( grep {$_!=$dd} (0..9) ) {
    last if $i-$c>2;
    $xx=$p; $xx=~s/$dd/$d/g;
    $c++ if exists $primes{$xx};
    $i++;
    next if $c<8;
    print "Answer to PE50 = $p";exit;
  }
}
