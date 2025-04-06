import ollama
from ollama import chat
from ollama import ChatResponse
import time
import json

ollama.pull("llama3.2")

PROMPT = json.loads("backend/prompts/anomyzation_prompts.json")
CONTEXTS = json.loads("backend/prompts/anomyzation_contexts.json")


# === Run test cases ===
results = []
for context in CONTEXTS:
    print(f"Running test for role: {context['role']} | task: {context['task']}")
    start_time = time.time()

    response: ChatResponse = chat(
        model=context["model"],
        messages=[{"role": "user", "content": PROMPT[0]["prompt"].format(context=context)}]
    )

    output_text = response.message["content"].strip()
    elapsed = round(time.time() - start_time, 2)

    results.append({
        "Role": context["role"],
        "Task": context["task"],
        "Variant": context["variant"],
        "Prompt": context["prompt"],
        "Response": output_text,
        "Latency (s)": elapsed,
        "Mean VRAM Usage": "TBD",  # Placeholder, needs system stats collection
        "Quality": None,
        "Accuracy": None,
        "Format/Usefulness": None,
        "Completeness": None,
        "Consistency": None,
        "Faithfulness": None,
        "Notes": ""
    })


print(results)