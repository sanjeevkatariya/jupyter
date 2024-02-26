#!/bin/zsh

# Check if two arguments are provided
if [ $# -ne 2 ]; then
    echo "Usage: $0 <URL> <output_filename>"
    exit 1
fi

# Assign arguments to variables
URL=$1
OUTPUT_FILE=$2

# Use curl to fetch the HTML content of the URL, then use sed to extract the text following the span with class "btext"
curl -s "$URL" | sed -n '/<span class="btext">/{s/.*&nbsp;//;s/<[^>]*>//g;p;}' | sed -E 's/\[[^]]+\]|\([^)]+\)//; s/The Orthodox Jewish Bible.*$//; s/T\.N\..*$//; s/%$//; s/%//g; s/\[|\]|\(|\)//g' > "$OUTPUT_FILE"
