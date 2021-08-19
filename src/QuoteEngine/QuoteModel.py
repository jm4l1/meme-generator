"""Quote Engine Module."""


class QuoteModel():
    """QuoteModel class."""

    def __init__(self, body: str, author: str) -> None:
        """Create a QouteModel.

        Parameters:
        body {str} : The body text of the quote.
        author {str} : The author of the quote.

        Returns:
        None

        Raises:
        None
        """
        self.body = body
        self.author = author
