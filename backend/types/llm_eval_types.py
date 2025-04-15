from pydantic import BaseModel


class EvalArgs(BaseModel):
    model: str

class Prompt(BaseModel):
    prompt: str

class Context(BaseModel):
    role: str
    task: str
    variant: str
    context: str
    hardware: str
    input_length: str