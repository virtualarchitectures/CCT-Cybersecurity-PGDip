#!/bin/bash

# Task: Display CPU usage.
echo "CPU Usage:"
top -bn1 | grep "Cpu(s)"