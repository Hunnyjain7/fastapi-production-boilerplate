import random
import string
from fastapi.responses import JSONResponse
import uuid


class Utility:
    @staticmethod
    def common_response(status, message, error, data):
        return JSONResponse({
            'status': status,
            'message': message,
            'error': error,
            'data': data,
        })

    @staticmethod
    def uuid():
        return str(uuid.uuid4())

    @staticmethod
    def generated_password():
        length = random.randint(8, 13)
        lower = string.ascii_lowercase
        upper = string.ascii_uppercase
        num = string.digits

        mix = 'FEN' + lower + upper + '@' + num
        temp = random.sample(mix, length)
        temp[6] = '@'
        password = "".join(temp)
        password = "FEN" + password
        return password


# print(Utility.uuid())
