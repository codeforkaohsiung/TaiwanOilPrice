my $s;

open(HTM, '20140419Brent') or die "$!";
while (defined($line = <HTM>)) {
	$s = $s.$line;
}
close(HTM);

print "\n========================\n";


my $last = "昨收";
my $range = index($s, $last);
#print ($s);
print ($range);

print "\n\n";

#print substr($s, $range + 30, 8);

#my $date = substr($s, $range + 30, 8);

my $date = substr($s, $range + 36, 8);

#print "\n\n";

#print substr($s, $range + 57, 6);

my $price = substr($s, $range + 63, 6);

my $tar = "Brent ".$date." ".$price;

print $tar;
print "\n========================\n";
print "\n\n";
