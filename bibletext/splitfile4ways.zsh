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

# Calculate the line numbers where to split the file (divide by 4 for four parts)
split_line1=$((num_lines / 4))
split_line2=$((2 * num_lines / 4))
split_line3=$((3 * num_lines / 4))

# Use csplit to split the file at the calculated line numbers
csplit "$input_file" $split_line1 $split_line2 $split_line3

# Rename the split files to reflect their parts
mv xx00 "${input_file}-part1.tmp"
mv xx01 "${input_file}-part2.tmp"
mv xx02 "${input_file}-part3.tmp"
mv xx03 "${input_file}-part4.tmp"

echo "File '$input_file' split into '${input_file}-part1.tmp', '${input_file}-part2.tmp', '${input_file}-part3.tmp', and '${input_file}-part4.tmp'"

