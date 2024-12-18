class HasChildError(Exception):
    def __init__(
        self,
        message="Record has associated records, deletion impossible"
    ):
        super().__init__(message)
