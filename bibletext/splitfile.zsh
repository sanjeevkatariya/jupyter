#!/bin/zsh

# Check if the correct number of arguments are provided
if [ "$#" -ne 1 ]; then
    echo "Usage: $0 <input_file>"
    exit 1
fi

# Extract the input file name from the command-line argument
input_file="$1"

# Count the number of lines in the input file
num_lines=$(wc -l < "$input_file")

# Calculate the line number where to split the file (divide by 2)
split_line=$((num_lines / 2))

# Split the file using csplit at the calculated line number
csplit "$input_file" $split_line

# Rename the split files
mv xx00 "${input_file}-part1.tmp"
mv xx01 "${input_file}-part2.tmp"

echo "File '$input_file' split into '${input_file}-part1.tmp' and '${input_file}-part2.tmp'"
