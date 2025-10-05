#!/bin/bash

# Task: Find files larger than 1MB.
echo "Finding files larger than 1MB:"
find /var/log -type f -size +1M