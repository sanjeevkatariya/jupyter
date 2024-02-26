import sys
import os
from openai import OpenAI

client = OpenAI(
    # This is the default and can be omitted
    api_key=os.environ.get("OPENAI_API_KEY"),
)

def file_to_mp3(directory_path, filename):
    """
    Simulated function to convert text to MP3.
    Replace this with your actual text-to-speech conversion logic.
    For demonstration, it returns 'MP3 data' as bytes.
    """
    file_path = os.path.join( directory_path, filename )
    print( "Reading from file:", file_path )
    """"
    Now read in the contents
    """
    try:
        file = open(file_path, 'r', encoding='utf-8')
        text_content = file.read()
    finally:
        file.close()
    """"
    Create the audio file
    """
    response = client.audio.speech.create(
        model="tts-1-hd",
        voice="onyx",
        input = text_content,
    )
    """
    Now create the mp3 filename
    """
    # Define MP3 output filename
    mp3_filename = os.path.splitext(filename)[0] + ".mp3"
    mp3_file_path = os.path.join(directory_path, mp3_filename)
    print( "Writing MP3 file: ", mp3_file_path )
    response.stream_to_file(mp3_file_path)
    return mp3_file_path

def process_files_in_directory(directory_path):
    """
    Reads text files from the specified directory, converts their content to MP3,
    and saves the MP3 files with the same base filename.
    """
    for filename in os.listdir(directory_path):
        if filename.endswith(".txt"):
            mp3_filename = file_to_mp3( directory_path, filename )
            print(f"Processed '{filename}' and saved to '{mp3_filename}'")

#
# Main Program starts here
# Invoke it as: python thisfile.pf directory_name
#
if len(sys.argv) > 1:
    directory_path = sys.argv[1]
else:
    directory_path = '.'
process_files_in_directory(directory_path)
