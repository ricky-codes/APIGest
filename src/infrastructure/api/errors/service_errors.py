class ServiceError(Exception):
    pass

class InsertError(ServiceError):
    description = "Error in insert operation"

class SelectError(ServiceError):
    description = "Error in select operation"

class UpdateError(ServiceError):
    description = "Error in update operation"

class DeleteError(ServiceError):
    description = "Error in delete operation"