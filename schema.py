from pydantic import BaseModel


class User(BaseModel):
    id: str
    username: str
    work: str

    class Config:
        orm_mode = True
