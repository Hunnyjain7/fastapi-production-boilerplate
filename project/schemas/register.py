from pydantic import BaseModel


class Register(BaseModel):
    email: str
    password: str
    user_name: str
    contact: int
