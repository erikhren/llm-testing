from pydantic import BaseModel


class EvalArgs(BaseModel):
    model: str

class Prompt(BaseModel):
    system_prompt: str

class Context(BaseModel):
    role: str
    task: str
    variant: str
    context: str
    hardware: str
    input_length: str