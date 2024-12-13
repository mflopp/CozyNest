class NoRecordsFound(Exception):
    """Exception for case when there are no records in the request."""
    def __init__(self, message="Not found", code=404):
        super().__init__(message, code)
