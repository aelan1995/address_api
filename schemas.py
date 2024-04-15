from pydantic import BaseModel

class UserSchema(BaseModel):
    id: int
    username: str
    name: str
    email: str
    nickname: str