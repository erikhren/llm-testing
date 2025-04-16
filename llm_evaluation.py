from argh import arg, dispatch_commands
import time

from backend.types.llm_eval_types import Context, EvalArgs, Prompt
from backend.util.eval_util import ensure_model_available, format_prompt, run_test, validate_data
from backend.util.file_util import load_json, save_results


PROMPTS = "./backend/prompts/anonymization_prompts.json"
CONTEXTS = "./backend/prompts/anonymization_contexts.json"


@arg('-m', '--model', help="Name of the LLM model to use (e.g., llama3, llama2).", default="llama3.2")
def evaluate(**kwargs):
    args = EvalArgs.model_validate(kwargs)

    results = []

    ensure_model_available(args.model)

    prompt_data_raw = load_json(PROMPTS)
    context_data_raw = load_json(CONTEXTS)

    prompt_data = validate_data(prompt_data_raw, Prompt, PROMPTS)
    context_data = validate_data(context_data_raw, Context, CONTEXTS)

    for prompt in prompt_data:

        for context in context_data:
            context_str = context.context
            # formatted_prompt = format_prompt(prompt_string, context_str)

            start_time = time.time()
            output = run_test(args.model, prompt.system_prompt, context_str)
            elapsed = round(time.time() - start_time, 2)

            results.append({
                "Role": context.role,
                "Task": context.task,
                "Variant": context.variant,
                "Prompt": prompt.system_prompt,
                "context": context_str,
                "Response": output,
                "Latency (s)": elapsed,
                # "Mean VRAM Usage": "TBD",
                "Quality": "",
                "Accuracy": "",
                "Format/Usefulness": "",
                "Completeness": "",
                "Consistency": "",
                "Faithfulness": "",
                "Notes": ""
            })

    print(results)

    save_results(results)


if __name__ == "__main__":
    dispatch_commands([evaluate])
