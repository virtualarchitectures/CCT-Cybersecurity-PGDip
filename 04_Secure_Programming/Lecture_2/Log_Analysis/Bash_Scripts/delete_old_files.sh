#!/bin/bash

# Task: Find and delete files older than 7 days in a directory.
echo "Finding and deleting files older than 7 days:"
find /tmp/old_files -type f -mtime +7 -delete