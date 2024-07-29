from pydantic import BaseModel


class Certidoes(BaseModel):
    filename: str
    url: str
