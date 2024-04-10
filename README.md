# Python-Thumb
Python application using pillow and pythumb to create thumbnails.

# How to use

## Clone project
```bash
git clone https://github.com/LucasSch2410/python-thumb.git
```

## Create a virtual environment
Windows
```bash
python -m venv .venv
.\.venv\Scripts\activate
pip install -r requirements.txt
```

Linux
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Setup the links and size
Just place the YouTube links you want to turn into thumbnails, one per line, in the links.txt file at the root of this project. 

The main.py file has a tuple variable named size. You can edit the size of the thumbnail.

## Run

```bash
python3 python-thumb/main.py
```

## Where see the thumbails?
The thumbnails will be inside the final_thumbs in data folder.