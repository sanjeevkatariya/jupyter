import sys
import os
from openai import OpenAI

client = OpenAI()

if len(sys.argv) != 3:
        print("Error: This script requires exactly 3 arguments.")
        sys.exit(1)  # Exit the script with a non-zero status to indicate an error

# The first command-line argument (excluding the script name) is accessible as sys.argv[1]
filename = sys.argv[1]
outputfilename = sys.argv[2]
print(f"Processing '{filename}'")
try:
    file = open(filename, 'r', encoding='utf-8')
    text_content = file.read()
finally:
    file.close()
#
# Create the Messge Block
#
response = client.chat.completions.create(
  model="gpt-4-turbo-preview",
  messages=[
    {
      "role": "system",
      "content": "Wherever you come across a hebrew word or hebrew name, right after it add in the word in english or english name in parentheses. If it already has an english word or name explanation present in parentheses following the Hebrew word, don't do anything. If you see the word G-d, replace it with Adonai (God)"
    },
    {
      "role": "user",
      "content": text_content
    },
  ],
  temperature=1,
  max_tokens=4095,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)
#
# Extracting the assistant's response
#
with open(outputfilename, 'w', encoding='utf-8') as file:
    file.write(response.choices[0].message.content)
