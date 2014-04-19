my $s;

open(HTM, '20130521USD-TWD') or die "$!";
while (defined($line = <HTM>)) {
	$s = $s.$line;
}
close(HTM);

print "=======================\n";
#print $s;
print "\n========================\n";


my $last = "Previous Close:";
my $range = index($s, $last);
print ($range);

print "\n\n";

print substr($s, $range + 35, 7);

print "\n\n";
