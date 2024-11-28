#!/bin/bash

# Report Generation Using awk
awk '
BEGIN {
    # Print the header of the report
    printf "Employee Report\n"
    printf "-------------------------------------\n"
    printf "%-10s %-15s %-10s %-10s\n", "ID", "Name", "Department", "Salary"
    printf "-------------------------------------\n"
}
NR > 1 { # Skip the header line
    printf "%-10s %-15s %-10s %-10s\n", $1, $2, $3, $4
}
END {
    print "-------------------------------------"
    print "End of Report"
}
' emp.txt

