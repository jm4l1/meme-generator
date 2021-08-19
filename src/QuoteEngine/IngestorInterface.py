"""Ingestor interface."""

from abc import ABC, abstractmethod
from pathlib import Path
from typing import List

from .QuoteModel import QuoteModel


class CannotIngestException(Exception):
    """Cannot Ingest Exception."""

    pass


class IngestorInterface(ABC):
    """Ingestor interface to provide base class for ingesting quotes from various sources.

    Concrete classes are should import the parse method.
    """

    allowed_extensions = []

    @classmethod
    def can_ingest(cls, path: str) -> bool:
        """Determine if give file can be ingested by the Interface implementation.

        Parameters:
        path {str} : The path of the input file to be tested.

        Returns
        True : if path is ingestible.
        False : if path is not ingestible.

        Raises:
        None
        """
        file_path = Path(path)
        if not file_path.exists():
            return False
        ext = path.split('.')[-1]
        return ext in cls.allowed_extensions

    @classmethod
    @abstractmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse input file into list of QuoteModel objects.

        Parameters:
        path {str} : The path of the input file to be tested.

        Returns
        list[QuoteModel] : list of model objects parse from file

        Raises:
        None
        """
        pass
