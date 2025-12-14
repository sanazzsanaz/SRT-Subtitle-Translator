SRT Subtitle Translator

This project is a Python script that automatically translates subtitle files in SRT format from English to Persian (Farsi) while preserving the original subtitle structure.

The script reads the subtitle file line by line, keeps subtitle numbers and time codes unchanged, and translates only the dialogue text using Google Translate via the deep-translator library.

Features

Translates English subtitles to Persian (Farsi) or any other language

Preserves SRT numbering and timestamps

Writes translated output incrementally (line by line)

Handles network or translation errors gracefully

Simple and beginner-friendly Python code

Requirements

Python 3.10+

Internet connection

Python package:

deep-translator

Install the dependency with:

pip install deep-translator

Usage

Place the following files in the same directory:

srt.py

harry.srt (input subtitle file)

Run the script:

python srt.py


After execution, a new file will be created:

harrynew.txt


This file contains the translated subtitles with the original SRT structure preserved.

How It Works

Lines containing only numbers are treated as subtitle indices.

Lines containing --> are treated as time codes.

Empty lines are preserved.

All other lines are translated from English to Persian and written to the output file.

A short delay is added between translation requests to avoid rate limiting.

Notes

Large subtitle files may take some time to process.

If a line fails to translate due to network issues, the original English line is written instead.

This project uses unofficial access to Google Translate and is intended for educational purposes.
