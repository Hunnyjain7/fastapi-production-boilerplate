from fastapi.responses import JSONResponse
import uuid


class Utility:
    @staticmethod
    def json_response(status, message, error, data):
        return JSONResponse({
            'status': status,
            'message': message,
            'error': error,
            'data': data,
        })

    @staticmethod
    def dict_response(status, message, error, data):
        return ({
            'status': status,
            'message': message,
            'error': error,
            'data': data,
        })

    @staticmethod
    def uuid():
        return str(uuid.uuid4())


print(Utility.uuid())
