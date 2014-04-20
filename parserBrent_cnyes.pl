my $s;

open(HTM, $ARGV[0]) or die "$!";
while (defined($line = <HTM>)) {
	$s = $s.$line;
}
close(HTM);

my $last = "昨收";
my $range = index($s, $last);
my $date = substr($s, $range + 36, 8);

print "date=".($date)."\n";
print "type=cnyes_Brent\n";
print "price=".substr($s, $range + 63, 6)."\n";
