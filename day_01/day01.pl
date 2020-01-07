#!/usr/bin/perl
# Advent of Code 2019
# Day 1

use strict;
use warnings;
use List::Util qw(sum);

open(my $in, "<", "input") or die "Can't open: $!";
chomp(my @mass = <$in>);
close $in;

sub fuel_count {
    my $num = shift;
    use integer;
    return $num / 3 - 2;
}

sub calculate_fuel_recursion {
    my $atomic_mass = shift;
    return $atomic_mass > 0 ? $atomic_mass + calculate_fuel_recursion(fuel_count($atomic_mass)) : 0;
}

print "Module fuel requirement: ", sum(map {fuel_count($_)} @mass), "\n";
print "Full fuel requirement: ", sum(map {calculate_fuel_recursion(fuel_count($_))} @mass), "\n";

