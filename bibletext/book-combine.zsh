#!/bin/zsh

# Check if no arguments were passed
if [ $# -eq 0 ]; then
  echo "Usage: $0 prefix"
  echo "Example: $0 genesis"
  exit 1
fi

prefix="$1"
list_file="mylist-${prefix}.txt"
output_file="${prefix}.mp3"

# Check if the list file exists
if [ ! -f "$list_file" ]; then
  echo "List file '$list_file' not found."
  exit 2
fi

# Execute ffmpeg command using the provided prefix for list and output files
ffmpeg -f concat -safe 0 -i "$list_file" -c copy "$output_file"

# Optional: Notify the user upon successful completion
echo "Concatenation complete: ${output_file} has been created."
