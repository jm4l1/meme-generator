# MEME Generator

## Overview

Meme generator – a multimedia application to dynamically generate memes, including an image with an overlaid quote.

## Supported Operated Systems

Implementation works with Linux and MacOS

## Dependencies for Running Locally

- pip 20.1.1
- Python >= 3.8.3
- virtualenv >= 20.0.23

## Basic Build Instructions

1. Clone this repo and change to directory.
2. Create virtual env: `virtualenv .`
3. Start virtualenv : `. bin/activate`
4. Install requirements: `pip install -r requirements.txt`
5. Run it.

## Project Sturcture

```
└── src
    ├── MemeEngine
    │   ├── MemeEngine.py
    │   ├── __init__.py
    ├── QuoteEngine
    │   ├── CSVIngestor.py
    │   ├── DOCXIngestor.py
    │   ├── Ingestor.py
    │   ├── IngestorInterface.py
    │   ├── PDFIngestor.py
    │   ├── QuoteModel.py
    │   ├── TXTIngestor.py
    │   ├── __init__.py
    ├── _data
    │   ├── DogQuotes
    │   ├── SimpleLines
    │   └── photos
    ├── app.py
    ├── fonts
    ├── meme.py
    ├── templates
    ├── test.py
    └── tmp
```
