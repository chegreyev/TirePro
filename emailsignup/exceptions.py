from rest_framework.exceptions import APIException, _get_error_details
from rest_framework import status

class LogInvalidationError(APIException):
    status_code = status.HTTP_403_FORBIDDEN
    default_detail = 'Login failed.'
    default_code = '403'

    def __init__(self, detail=None, code=None):
        if detail is None:
            detail = self.default_detail
        if code is None:
            code = self.default_code

        err = dict()
        err['resultCode'] = 1
        err['messages'] = [detail]
        err['data'] = {}

        self.detail = err


