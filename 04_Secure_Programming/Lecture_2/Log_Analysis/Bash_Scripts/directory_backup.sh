#!/bin/bash

# Task: Create a backup of a directory.
echo "Creating a backup of /etc/my_config:"
tar -czvf my_config_backup.tar.gz /etc/my_config
