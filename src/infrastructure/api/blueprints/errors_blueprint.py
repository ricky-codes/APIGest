from flask import Blueprint
from flask import jsonify

from src.infrastructure.api.errors import service_errors
from src.infrastructure.api.errors import api_errors

errors = Blueprint("erros", __name__)

@errors.app_errorhandler(service_errors.ServiceError)
@errors.app_errorhandler(api_errors.ApiError)
def handle_error(error):
    message = [str(x) for x in error.args]
    status_code = 500
    success = False
    response = {
        'success': success,
        'error': {
            'type': error.__class__.__name__,
            'message': message
        }
    }

    return jsonify(response), status_code