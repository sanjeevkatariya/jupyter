#!/bin/zsh

# Check if at least 2 arguments are provided (1 output and 1 or more input files)
if [ "$#" -lt 2 ]; then
    echo "Usage: $0 <input1.mp3> ... <inputN.mp3> <output.mp3>"
    exit 1
fi

# Extract the last argument as the output file name
output_file=${@: -1}

# Build the input string for ffmpeg by concatenating all but the last argument
input_files=""
for arg in "$@"
do
    if [[ "$arg" != "$output_file" ]]; then
        if [[ -z "$input_files" ]]; then
            input_files="$arg"
        else
            input_files+="|$arg"
        fi
    else
        # Break the loop if we reach the last argument to avoid adding the output file to input_files
        break
    fi
done

echo "Input Files:" $input_files
echo "Output File:" $output_file
 
# Combine the MP3 files
ffmpeg -i "concat:$input_files" -acodec copy "$output_file"
