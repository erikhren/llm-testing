import time
from typing import Any, Dict, List, Type
import ollama
from pydantic import BaseModel, ValidationError


def format_prompt(prompt: str, context: str) -> str:
    return prompt.format(context=context)


def run_test(model: str, prompt: str) -> str:
    msg = [{"role": "user", "content": prompt}]
    response = ollama.chat(model=model, messages=msg)
    return response.message["content"]

def ensure_model_available(model: str):
    start_time = time.time()

    response = ollama.list()

    if isinstance(response, tuple):
        models_list = response[0]
    else:
        models_list = response

    existing_models = [m.model for m in models_list]
        
    if model in existing_models:
        print(f"Model '{model}' is already available locally.")
    else:
        print(f"Model '{model}' not found locally. Pulling now...")
        ollama.pull(model)

    elapsed = round(time.time() - start_time, 2)
    print(f"Time elapsed to init the model {model}: {elapsed} seconds")


def validate_data(data: List[Dict[str, Any]], schema: Type[BaseModel], source: str) -> List[BaseModel]:
    try:
        return [schema(**item) for item in data]
    except ValidationError as e:
        raise RuntimeError(f"Validation failed for {source}:\n{e}")
