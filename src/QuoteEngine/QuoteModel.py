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

    def __str__(self) -> str:
        """Print readable string representation of quote.

        Parameters:
        None

        Returns:
        str : Quote in the for '{body}' - {author}

        Raises:
        None
        """
        return f'"{self.body}" - {self.author}'

    def __repr__(self) -> str:
        """Print machine readable representation of quote.

        Parameters:
        None

        Returns:
        str : QuoteModel(body={body},author={author})

        Raises:
        None
        """
        return f'QuoteModel(body={self.body},author={self.author})'
