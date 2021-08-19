"""CSV Ingestor."""


from typing import List
from csv import DictReader

from .IngestorInterface import IngestorInterface, CannotIngestException
from .QuoteModel import QuoteModel


class CSVIngestor(IngestorInterface):
    """Concrete Implementation of IngestorInterface for ingesting CSV type files."""

    allowed_extensions = ['csv']

    def __init__(self):
        """Create CSVIngestor."""
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
        with open(path, 'r') as input_file:
            for row in DictReader(input_file):
                quotes.append(QuoteModel(**row))
        return quotes
