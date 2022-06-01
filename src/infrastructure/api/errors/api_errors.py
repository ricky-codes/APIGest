class ApiError(Exception):
    pass

class DbOperationError(ApiError):
    code = 403
    description = "Database operation error"