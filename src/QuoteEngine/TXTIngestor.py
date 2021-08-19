"""TXT Ingestor."""

from typing import List

from .IngestorInterface import IngestorInterface, CannotIngestException
from .QuoteModel import QuoteModel


class TXTIngestor(IngestorInterface):
    """Concrete Implementation of IngestorInterface for ingesting TXT type files."""

    allowed_extensions = ['txt']

    def __init__(self):
        """Create TXTIngestor."""
        pass

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse input file into list of QuoteModel objects.

        Parameters:
        path {str} : The path of the input file to be tested.

        Returns
        list[QuoteModel] : list of model objects parse from file

        Raises:
        CannotIngestException
        """
        if not cls.can_ingest(path):
            raise CannotIngestException('cannot ingest exception')

        quotes = []
        with open(path, 'r') as input_file:
            row = input_file.readline().strip()
            while row:
                body, author = row.split("-")
                body = body.replace("\"", "")
                quotes.append(QuoteModel(body, author))
                row = input_file.readline().strip()

        return quotes
