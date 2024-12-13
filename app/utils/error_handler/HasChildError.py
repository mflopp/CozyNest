class HasChildError(Exception):
    def __init__(
        self,
        message="Records has associated records, deletion impossible",
        code=409
    ):
        super().__init__(message, code)
