#!/bin/bash
# --- Bash Exercises - Basic Command Chaining - Extract usernames ---

echo "Extracting usernames from /etc/passwd:"
cut -d: -f1 /etc/passwd > usernames.txt
cat usernames.txt