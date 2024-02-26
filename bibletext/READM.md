The collection basically "crawls" https://biblehub.com/ojb/. You invoke it by typing in:
            ./processbook.zsh genesis 1 40 
Basically
            ./processbook.zsh book-you-want starting-chapter-number ending-chapter-number
The magic
1. It crawls the url given above and pulls down the content.
2. Then cleans it up removing HTML
3. Then using chatGPT augments it ( taking words in Hebrew but adding in English translations )
4. Then splits up the final file ( e.g. genesis-1, genesis-2 ) and then produce mp3 files using whisper ( tts-1-hd )
5. Then uses ffmpeg and binds the two together to produce genesis-1.mp3

Basically in a short while - you have the entire bible for which there isn't a proper reading - but using AI!
