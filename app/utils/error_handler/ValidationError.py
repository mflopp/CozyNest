class ValidationError(Exception):
    """
    Exception raised for validation errors.

    Attributes:
        text (str): The error text.
    """

    def __init__(self, text: str):
        """
        Initializes the ValidationError with a given error text.

        Args:
            text (str): The error text describing the issue.
        """
        super().__init__(text)
        self.text: str = text
