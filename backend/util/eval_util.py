import time
import ollama


def format_prompt(prompt: str, context: str) -> str:
    return prompt.format(context=context)


def run_test(model: str, prompt: str) -> str:
    msg = [{"role": "user", "content": prompt}]
    response = ollama.chat(model=model, messages=msg)
    return response.message["content"]

def ensure_model_available(model: str):
    start_time = time.time()

    existing_models = [m["name"] for m in ollama.list()["models"]]
    if model in existing_models:
        print(f"Model '{model}' is already available locally.")
    else:
        print(f"Model '{model}' not found locally. Pulling now...")
        ollama.pull(model)

    elapsed = round(time.time() - start_time, 2)
    print(f"Time elapsed to init the model {model}: {elapsed} seconds")
