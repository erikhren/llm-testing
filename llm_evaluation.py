import argh
import time

from backend.util.eval_util import ensure_model_available, format_prompt, run_test
from backend.util.file_util import load_json, save_results


PROMPTS = "./backend/prompts/anonymization_prompts.json"
CONTEXTS = "./backend/prompts/anomyzation_contexts.json"


# @argh.arg('-m', '--model', help="Name of the LLM model to use (e.g., llama3, llama2).", default="llama3.2")
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
