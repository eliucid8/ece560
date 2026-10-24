#!/bin/bash

    FILE_TO_WATCH="../../cryptotest-report.txt" # Replace with the actual file path
    COUNT_FILE="./opencount"  # File to store the count

    # Initialize count file if it doesn't exist
    if [ ! -f "$COUNT_FILE" ]; then
        echo 0 > "$COUNT_FILE"
    fi

    echo "Monitoring $FILE_TO_WATCH for open events..."

    while inotifywait -e close_write "$FILE_TO_WATCH"; do
        CURRENT_COUNT=$(cat "$COUNT_FILE")
        NEW_COUNT=$((CURRENT_COUNT + 1))
        echo "$NEW_COUNT" > "$COUNT_FILE"
        echo "$FILE_TO_WATCH written/closed $NEW_COUNT times"
    done
