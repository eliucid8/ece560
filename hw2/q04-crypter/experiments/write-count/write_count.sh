#!/bin/bash

# Specify the file to monitor
FILE_TO_WATCH="/path/to/your/file.txt"

# Initialize a counter for write events
WRITE_COUNT=0

# Loop indefinitely, watching for 'close_write' events
while inotifywait -e close_write "$FILE_TO_WATCH" &>/dev/null; do
  ((WRITE_COUNT++))
  echo "File '$FILE_TO_WATCH' has been written to $WRITE_COUNT times."
done
