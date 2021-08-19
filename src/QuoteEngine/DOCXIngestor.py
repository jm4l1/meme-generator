"""DOCX Ingestor."""

from typing import List
from .IngestorInterface import IngestorInterface, CannotIngestException
from .QuoteModel import QuoteModel

from docx import Document


class DOCXIngestor(IngestorInterface):
    """Concrete Implementation of IngestorInterface for ingesting Docx type files."""

    allowed_extensions = ['docx']

    def __init__(self):
        """Create DOCXIngestor."""
        pass

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse input file into list of QuoteModel objects.

        Arguments:
        path {str} : The path of the input file to be tested.

        Returns
        list[QuoteModel] : list of model objects parse from file

        Raises:
        CannotIngestException
        """
        if not cls.can_ingest(path):
            raise CannotIngestException('cannot ingest exception')

        quotes = []
        document = Document(path)
        for paragraph in document.paragraphs:
            if paragraph.text:
                body, arthor = paragraph.text.split("-")
                body = body.replace("\"", "")
                quotes.append(QuoteModel(body, arthor))
        return quotes
