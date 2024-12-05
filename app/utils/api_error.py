class ValidationError(Exception):
    """Custom exception for validation errors."""
    def __init__(self, details: str):
        """
        Initialize the exception with error details.

        Args:
            details (str): A description of the error.
        """
        self.details = details
