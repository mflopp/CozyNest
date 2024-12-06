from typing import Dict, Any


class ValidationError(Exception):
    """
    Exception raised for validation errors.

    Attributes:
        title (str): The title of the error.
        message (str): The detailed error message.
        code (int): The error code.
    """

    def __init__(self, details: Dict[str, Any]):
        """
        Initializes the ValidationError with error details.

        Args:
            details (Dict[str, Any]): A dictionary containing error details.
                It must include the keys 'title', 'message', and 'code'.

        Raises:
            KeyError: If the required keys are missing in the details
                      dictionary.
        """
        if not all(key in details for key in ('title', 'message', 'code')):
            msg = "Details must contain 'title', 'message', and 'code'."
            raise KeyError(msg)

        super().__init__(details.get('message', 'Validation error occurred.'))

        self.title: str = details['title']
        self.message: str = details['message']
        self.code: int = details['code']


def get_details(title: str, message: str, code: int):
    details = {
        'title': title,
        'message': message,
        'code': code
    }

    return details