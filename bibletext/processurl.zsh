#!/bin/zsh

# Check if two arguments are provided
if [ $# -ne 2 ]; then
    echo "Usage: $0 <URL> <chaptername>"
    exit 1
fi

# Assign arguments to variables
URL=$1
CHAPTER_NAME=$2

# Use curl to fetch the HTML content of the URL, then use sed to extract the text following the span with class "btext"
curl -s "$URL" | sed -n '/<span class="btext">/{s/.*&nbsp;//;s/<[^>]*>//g;p;}' | sed -E 's/\[[^]]+\]|\([^)]+\)//; s/The Orthodox Jewish Bible.*$//; s/T\.N\..*$//; s/%$//; s/%//g; s/\[|\]|\(|\)//g' > "$CHAPTER_NAME".tmp
python fixtext.py $CHAPTER_NAME.tmp $CHAPTER_NAME
rm $CHAPTER_NAME.tmp
./splitfile.zsh $CHAPTER_NAME
python biblereading-singlefile.py $CHAPTER_NAME-part1.tmp
python biblereading-singlefile.py $CHAPTER_NAME-part2.tmp
./combinemp3s.zsh $CHAPTER_NAME-part1.mp3 $CHAPTER_NAME-part2.mp3 $CHAPTER_NAME.mp3 
