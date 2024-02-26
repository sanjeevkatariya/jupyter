import sys
import os
from openai import OpenAI

client = OpenAI(
    # This is the default and can be omitted
    api_key=os.environ.get("OPENAI_API_KEY"),
)

def file_to_mp3(filename):
    """
    Simulated function to convert text to MP3.
    Replace this with your actual text-to-speech conversion logic.
    For demonstration, it returns 'MP3 data' as bytes.
    And read in the contents
    """
    if os.path.exists(filename):
        print(f"Processing '{filename}'")
        try:
            file = open(filename, 'r', encoding='utf-8')
            text_content = file.read()
        finally:
            file.close()
        """"
        Create the audio file
        """
        mp3_filename = os.path.splitext(filename)[0] + ".mp3"
        print( "Will write the output to MP3 file: ", mp3_filename )

        with client.audio.speech.with_streaming_response.create(
            model="tts-1-hd",
            voice="onyx",
            speed="0.85",
            input = text_content,
        ) as response:
            # This doesn't seem to be *actually* streaming, it just creates the file
            # and then doesn't update it until the whole generation is finished
            response.stream_to_file(mp3_filename)

        print(f"Processed '{filename}' and saved to '{mp3_filename}'")
        return mp3_filename
    else:
        print(f"Error: The file '{filename}' does not exist.")
#
# Main Program starts here
# Invoke it as: python thisfile.pf filename
#
if len(sys.argv) > 1:
    inputfile = sys.argv[1]
file_to_mp3(inputfile)
