#!/bin/zsh

# Check if no arguments were passed
if [ $# -eq 0 ]; then
  echo "Usage: $0 base_filename"
  echo "Example: $0 genesis"
  exit 1
fi

# Assuming $1 is the first argument passed to the script
base="$1"

ffmpeg -loop 1 -i "${base}.webp" -i "${base}.mp3" -c:a aac -b:a 128k -c:v libx264 -tune stillimage -shortest -pix_fmt yuv420p -vf "scale=trunc(iw/2)*2:trunc(ih/2)*2" "${base}.mp4"
