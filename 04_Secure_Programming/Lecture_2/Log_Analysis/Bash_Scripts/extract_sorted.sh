#!/bin/bash

echo "Extracting and sorting error lines from logfile.txt:"
grep "error" logfile.txt | sort
