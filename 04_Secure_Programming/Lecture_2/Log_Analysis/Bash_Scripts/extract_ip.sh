#!/bin/bash

# Task: Extract unique IP addresses from a log file.
echo "Extracting unique IP addresses from logfile.txt:"
grep -oE '([0-9]{1,3}\.){3}[0-9]{1,3}' logfile.txt | sort -u
