import subprocess

MODELS = {
    "llama": "llama3",
    "mistral": "mistral",
    "phi": "phi"
}

def ask_model(model_name, question):
    result = subprocess.run(
        ["ollama", "run", model_name, question],
        capture_output=True,
        text=True
    )
    return result.stdout.strip()

def collect_responses(question):
    responses = {}
    for label, model in MODELS.items():
        responses[label] = ask_model(model, question)
    return responses
