my $s;

open(HTM, $ARGV[0]) or die "$!";
while (defined($line = <HTM>)) {
	$s = $s.$line;
}
close(HTM);

my $time = "quoteTime";
my $range = index($s, $time);
#my $date = substr($s, $range + 20, 10);
#print "date=".($date)."\n";

my $year = substr($s, $range + 20, 4);
my $mm = substr($s, $range + 25, 2);
my $dd = substr($s, $range + 28, 2);

print "date=".($year).($mm).($dd)."\n";
print "type=bloomberg_USDTWD\n";

my $last = "Previous Close:";
my $range = index($s, $last);

print "price=".substr($s, $range + 35, 7)."\n";
