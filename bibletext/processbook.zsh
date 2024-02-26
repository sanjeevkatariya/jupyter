#!/bin/zsh

# Check if at least 3 arguments are provided
if [ "$#" -ne 3 ]; then
    echo "Usage: $0 <name> <startnumber> <endnumber>"
    exit 1
fi

# Extract arguments
name=$1
startnumber=$2
endnumber=$3

# Loop from 1 to the specified number
for i in $(seq $startnumber $endnumber); do
    # Construct the URL
    url="https://biblehub.com/ojb/${name}/${i}.htm"
    # Construct the chaptername
    chapter_file="${name}-${i}"
    # Call the processing script with the URL and output filename
    ./processurl.zsh "$url" "$chapter_file"
done
