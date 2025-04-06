import argh
from typing import Optional
import time

import ollama

from backend.util.eval_util import ensure_model_available, format_prompt, run_test
from backend.util.file_util import load_json, save_results


PROMPTS = "backend/prompts/anomyzation_prompts.json"
CONTEXTS = "backend/prompts/anomyzation_contexts.json"


@argh.arg('-m', '--model', help="Name of the LLM model to use (e.g., llama3, llama2).", default="llama3.2")
def evaluate(
    model: str
):
    results = []

    ensure_model_available(model)
    prompt_data = load_json(PROMPTS)
    context_data = load_json(CONTEXTS)

    for p in prompt_data:
        prompt = p["prompt"]

        for c in context_data:
            context = c["context"]

            formatted = format_prompt(prompt, context)

            start_time = time.time()
            output = run_test(model, formatted)
            elapsed = round(time.time() - start_time, 2)

            results.append({
                "Role": context["role"],
                "Task": context["task"],
                "Variant": context["variant"],
                "Prompt": context["prompt"],
                "Response": output,
                "Latency (s)": elapsed,
                # "Mean VRAM Usage": "TBD",
                "Quality": None,
                "Accuracy": None,
                "Format/Usefulness": None,
                "Completeness": None,
                "Consistency": None,
                "Faithfulness": None,
                "Notes": ""
            })

    print(results)

    save_results(results)




if __name__ == "__main__":
    argh.dispatch_command(evaluate)


# # do I create an env?
# # Should this be cli? --> models list, prompt --> paste it? or select it from json?
# # seperation of concents --> util functions

# PROMPT = json.loads("backend/prompts/anomyzation_prompts.json")  # Better way?
# CONTEXTS = json.loads("backend/prompts/anomyzation_contexts.json")
# MODEL = "llama3.2" # iterable?

# ollama.pull(MODEL)  # we can delete it after + time how long it takes to init?

# # Model parameters?

# # === Run llm evaluation ===
# results = []
# for context in CONTEXTS:
#     print(f"Running test for role: {context['role']} | task: {context['task']}")
#     start_time = time.time()

#     response: ChatResponse = chat(
#         model=MODEL,
#         messages=[{"role": "user", "content": PROMPT[0]["prompt"].format(context=context)}]
#     )

#     output_text = response.message["content"].strip()
#     elapsed = round(time.time() - start_time, 2)

#     # storing alternatives // better
#     results.append({
#         "Role": context["role"],
#         "Task": context["task"],
#         "Variant": context["variant"],
#         "Prompt": context["prompt"],
#         "Response": output_text,
#         "Latency (s)": elapsed,
#         "Mean VRAM Usage": "TBD",  # Placeholder, needs system stats collection
#         "Quality": None,
#         "Accuracy": None,
#         "Format/Usefulness": None,
#         "Completeness": None,
#         "Consistency": None,
#         "Faithfulness": None,
#         "Notes": ""
#     })

# # save file just in case
# print(results)