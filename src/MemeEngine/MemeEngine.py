"""Meme Engine Module."""
from PIL import Image, ImageDraw, ImageFont
from pathlib import Path

FONT_PATH = Path("./fonts").absolute()


class MemeEngine():
    """Meme Engine class."""

    def __init__(self, out_path: str) -> None:
        """Create MemeEngine.

        Parameters:
        out_path {str} : path to which generated memes will be saved.

        Returns:
        None

        Raises:
        None
        """
        self.out_path = out_path

    def make_meme(self, img_path, text, author, width=500) -> str:
        """Create a meme from a given image and text.

        Parameters:
        img_path {str} : path to img file to be used in meme.
        text {str} : text of quote to be used in meme.
        author {str} : author of quote to be used in meme.
        author {int} : Width of the meme image [default = 500].

        Returns:
        None

        Raises:
        None
        """
        # open file
        img = Image.open(img_path)

        # resize Image to width
        ratio = width/float(img.size[0])
        height = int(ratio*float(img.size[1]))
        img = img.resize((width, height), Image.NEAREST)

        # add text
        draw = ImageDraw.Draw(img)
        print(FONT_PATH)
        font = ImageFont.truetype(
            f'{FONT_PATH}/Roboto-BoldItalic.ttf', size=40)
        draw.text((10, height/2),
                  f'{text} - {author}', fill='white', font=font)

        # save image
        img.save(f'{self.out_path}/{img_path.split("/")[-1]}')
        # return image path
        return img_path
