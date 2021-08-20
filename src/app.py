import random
import os
import requests
from flask import Flask, render_template, abort, request
from datetime import datetime

from MemeEngine import MemeEngine
from QuoteEngine import Ingestor
from QuoteEngine.QuoteModel import QuoteModel

app = Flask(__name__)

meme = MemeEngine('./static')


def setup():
    """ Load all resources """

    quote_files = ['./_data/DogQuotes/DogQuotesTXT.txt',
                   './_data/DogQuotes/DogQuotesDOCX.docx',
                   './_data/DogQuotes/DogQuotesPDF.pdf',
                   './_data/DogQuotes/DogQuotesCSV.csv']
    ingestor = Ingestor()
    quotes = []
    for file in quote_files:
        try:
            quotes = [*quotes, *ingestor.parse(file)]
        except:
            continue
    images_path = "./_data/photos/dog/"

    imgs = [f'{images_path}{img_name}' for img_name in os.listdir(images_path)]

    return quotes, imgs


quotes, imgs = setup()


@app.route('/')
def meme_rand():
    """ Generate a random meme """

    quotes, imgs = setup()
    img = random.choice(imgs)
    quote = random.choice(quotes)
    path = meme.make_meme(img, quote.body, quote.author)
    return render_template('meme.html', path=path)


@app.route('/create', methods=['GET'])
def meme_form():
    """ User input for meme information """
    return render_template('meme_form.html')


@app.route('/create', methods=['POST'])
def meme_post():
    """ Create a user defined meme """

    image_url = request.form.get('image_url')
    body = request.form.get('body')
    author = request.form.get('author')
    data = requests.get(image_url, allow_redirects=True)
    d = datetime.now()
    file_name = f'./tmp/img_{d.strftime("%Y%m%d_%H%M%S%f")}.png'
    with open(f'{file_name}', 'wb') as img_file:
        img_file.write(data.content)

    path = meme.make_meme(file_name, body, author)
    os.remove(file_name)
    return render_template('meme.html', path=path)


if __name__ == "__main__":
    app.run()
