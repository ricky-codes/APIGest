class Error(Exception):
    pass


class NotFoundError(Error):
    pass

class EmptySetError(Error):
    pass

class QueryError(Error):
    pass