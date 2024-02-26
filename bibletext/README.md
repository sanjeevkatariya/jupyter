# BibleText Reader

The BibleText Reader is a powerful tool designed to bring the Bible's text to life in a new and innovative way. This tool leverages the capabilities of modern AI to enhance the reading experience, making it more accessible and engaging. Here's how it works:

## Invocation

Invoke the tool by typing in the command line:

./processbook.zsh <book-you-want> <starting-chapter-number> <ending-chapter-number>


For example, to process the Book of Genesis, chapters 1 through 40:

./processbook.zsh Genesis 1 40


## Process Overview

1. **Crawl Content**: The tool crawls https://biblehub.com/ojb/ to pull down the content for the specified book and chapters.

2. **Clean HTML**: It then cleans up the content by removing HTML artifacts, ensuring the text is clean and readable.

3. **Augment with ChatGPT**: Using ChatGPT, the tool augments the text by identifying words in Hebrew and adding their English translations in parentheses. This step enriches the text, making it more accessible to a broader audience.

4. **Split and Process Text**: The cleaned and augmented text is split into individual chapters (e.g., genesis-1, genesis-2, etc.).

5. **Text-to-Speech Conversion**: Each chapter is then converted into an MP3 file using Whisper (tts-1-hd), creating high-quality audio versions of the text.

6. **Audio Processing**: Using FFmpeg, the tool binds the audio files together to produce a single MP3 file for each chapter, like genesis-1.mp3.

## Outcome

In a short while, you have the entire Bible—or any specified portion of it—available in a format that combines the richness of its original languages with the accessibility of English translations, all brought to life through audio. This innovative approach leverages AI to create a new reading experience for texts where traditional readings may not be readily available.
