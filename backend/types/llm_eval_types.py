from pydantic import BaseModel


class EvalArgs(BaseModel):
    model: str