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

## Modules

QuoteEngine: responsible for ingesting many types of files that contain quotes. A `QuoteModel` represents a quote which is a string of text and an author `"This is a quote body" - Author`. The `IngestorInterface` is an abstract class providing functionality for extracting quotes from various file types. This class includes the method `can_ingest` , which is implemented by the base class to check if a given file can be ingested by an `IngestorInterface`. The method `parse` is abstract in the base class and must be implemented in any derived classes of the `IngestorInterface` type. This method reads the input file to produce a list of `QuoteModel` objects.

The `CSVIngestor.py`, `DOCXIngestor.py`, `PDFIngestor.py` and `TXTIngestor.py` are `IngestorInterface` types that parse `csv`, `docx`, `pdf` and `txt` files repectively. The `Ingestor.py` provides a general interface that accepts a given file type and parses it with the correct ingestor. If the file cannot be ingested a `CannotIngestException` exception is returned.

MemeEngine : responsible for manipulating and drawing text onto images. The `MemeEngine` class, loads a file from a given locations, palces the specified quote (text , author) onto the image to create a meme, saves the meme to a location specifed at class creation and returns the path of the meme.

## Dependencies for Modules

    - Pillow (pip install)
    - python-docx (pip install)
    - pdftotext cli tool

## Using the modules
