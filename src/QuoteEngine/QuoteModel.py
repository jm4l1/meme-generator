"""Quote Engine Module."""


class QuoteModel():
    """QuoteModel class."""

    def __init__(self, body: str, author: str) -> None:
        """Create a QouteModel.

        Arguments:
        body {str} : The body text of the quote.
        author {str} : The author of the quote.

        Returns:
        None

        Raises:
        None
        """
        self._body = body
        self._author = author
