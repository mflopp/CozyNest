class NoRecordsFound(Exception):
    """Exception for case when there are no records in the request."""
    def __init__(self, message="No Records Found"):
        super().__init__(message)
