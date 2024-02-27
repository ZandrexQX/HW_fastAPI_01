from pydantic import BaseModel


class User(BaseModel):
    id: int
    name: str
    surname: str
    email: str
    password: str


    def __repr__(self):
        return f"User {self.name} - {self.id}"
