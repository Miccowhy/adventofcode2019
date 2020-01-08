#!/usr/bin/perl
# Advent of Code 2019
# Day 3

use strict;
use warnings;
use List::Util qw(min);
use List::MoreUtils qw(first_index);
#use Set::Light;
#use Set::Intersection;
use Array::Utils qw(:all);
use Math::Complex;

sub split_data {
    return map {split /,/} @_;
}

sub closest_manhattan_distance {
    my @first = $_[0];
    my @second = $_[1];
    my @zeros = (0, 0);
    my @intersection = intersect(@first, @second);
    my @minus = array_minus(@intersection, @zeros);
    return min(map {abs($_[0]) + abs($_[1])} @minus);
}

sub step_count {
    my @first = $_[0];
    my @second = $_[1];
    my @zeros = (0, 0);
    my @intersection = intersect(@first, @second);
    my @minus = array_minus(@intersection, @zeros);
    return min(map {my $one = $_[0]; my $two = $_[1];
        firstindex {$_[0] == $one} @first + firstindex{$_[1] == $two} @second} @minus);
}

sub path {
    my %directions = (
        R => 1,
        L => -1,
        U => 1*i,
        D => -1*i
    );
    my @wiring = ([0, 0]);
    
    for my $move (@_) {
        my $vector = substr $move, 0, 1;
        my $magnitude = (substr $move, 1);
        for my $i (0 .. $magnitude) {
            push(@wiring, ($wiring[-1][0] + Re($directions{$vector}), $wiring[-1][1] + Im($directions{$vector})));
        }
    }
    return @wiring;
} 

sub unpack_paths {
    open(my $in, "<", "input") or die "Can't open: $!";
    chomp(my @wires = <$in>);
    close $in;
    return map {split /,/, $_} @wires;
}

my @wires = unpack_paths();
print scalar(@wires), "\n";
print "Manhattan distance: ", closest_manhattan_distance(@wires), "\n";
print "Step count: ", step_count(@wires), "\n";

