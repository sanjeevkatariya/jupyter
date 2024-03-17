#!/bin/zsh

# Check if no arguments were passed
if [ $# -eq 0 ]; then
  echo "Usage: $0 prefix"
  echo "Example: $0 genesis"
  exit 1
fi

prefix="$1"
list_file="mylist-${prefix}.txt"

# Ensure the file doesn't exist
rm -f "$list_file"

# Loop through files with the prefix and a specific pattern
for f in "${prefix}"-*.mp3; do
  echo "file '$f'" >> "$list_file"
done

# Optional: Check if mylist.txt is empty or not created, indicating no files matched
if [ ! -s "$list_file" ]; then
  echo "No files found with the prefix '${prefix}'."
  rm "$list_file"  # Cleanup the empty list file
fi

