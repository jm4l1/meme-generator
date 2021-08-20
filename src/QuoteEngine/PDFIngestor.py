"""PDF Ingestor."""

from subprocess import run, PIPE
from typing import List

from .IngestorInterface import IngestorInterface, CannotIngestException
from .QuoteModel import QuoteModel


class PDFIngestor(IngestorInterface):
    """Concrete Implementation of IngestorInterface for ingesting PDF type files."""

    allowed_extensions = ['pdf']

    def __init__(self):
        """Create PDFIngestor."""
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

        try:
            quotes = []
            command = run(['pdftotext', '-enc', 'UTF-8', '-eol', 'mac',
                           path, '-'], stdout=PIPE)
            output = command.stdout.decode(
                'utf-8').strip().split(" \"")
            for row in output:
                body, author = row.split("-")
                body = body.replace("\"", "")
                quotes.append(QuoteModel(body, author))
            return quotes
        except Exception as e:
            print(e)
            raise Exception("Error while parsing")
