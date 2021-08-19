"""Generic Ingestor."""

from typing import List

from .IngestorInterface import CannotIngestException, IngestorInterface
from .CSVIngestor import CSVIngestor
from .DOCXIngestor import DOCXIngestor
from .PDFIngestor import PDFIngestor
from .TXTIngestor import TXTIngestor
from .QuoteModel import QuoteModel


class Ingestor(IngestorInterface):
    """Implementation of IngetorInterface to perform generic ingestion."""

    ingestors = [CSVIngestor, DOCXIngestor, PDFIngestor, TXTIngestor]

    def __init__(self):
        print("creating Ingestor")

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse input file into list of QuoteModel objects.

        Arguments:
        path {str} : The path of the input file to be tested.

        Returns
        list[QuoteModel] : list of model objects parse from file

        Raises:
        None
        """
        print(f"parsing path at {path}")
        for ingestor in cls.ingestors:
            if ingestor.can_ingest(path):
                try:
                    return ingestor.parse(path)
                except CannotIngestException as e:
                    return e
                except:
                    raise Exception("Unable to parse file")
            else:
                raise CannotIngestException("File cannot be ingested")
