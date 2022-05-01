# HTHS-Bot
## HTHS Class of 2025 Discord Bot v0.3.2

Features:
- Repeat a message in a text or voice channel.
- Tint an image a certain color.
- Scramble a message.

Commands:
- \\echo **message** - echoes message
- \\help - displays this help message
- \\leave - leaves your voice channel
- \\say **message** - says a message in your voice channel
- \\scramble **message** - scramble text
- \\tint **hexcolor** **imageurl** - tints image by a color (*Must be URL!*)

## Installation (Windows 10)
1. Download and extract the source code.
2. Run `py -m pip install -r requirements.txt` to install all required libraries.
3. Download an executable for ffmpeg and move it into the same directory as the source code.
4. Open `main.py`.

## Installation (macOS)
1. Open Terminal
2. Either:
  a. Install the command line dev tools by running `python3 --help > /dev/null`
  b. Install Python from Python.org
  NEVER use the built in Python; the version is outdated.
3. Run the following terminal command: `curl -LJO https://github.com/MathIsFun0/HTHS-Bot/archive/refs/heads/main.zip; mv main.zip hthsbot0.3.1.zip; unzip hthsbot0.3.1.zip; rm hthsbot0.3.1.zip; cd hthsbot0.3.1; pip3 install -r requirements.txt; cd ..`
4. When you want to run the program, run `python3 hthsbot0.3.1/main.py`
