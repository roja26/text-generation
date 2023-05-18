from fastapi import FastAPI
import requests

app = FastAPI()

INFERENCE_API = "https://api-inference.huggingface.co/models/sshleifer/tiny-gpt2/default"


@app.post("/predict/")
async def run_inference(request_data: dict):
    hf_pipeline = "text-generation"
    model_deployed_url = INFERENCE_API
    inputs = request_data["inputs"]
    parameters = request_data.get("parameters", {})

    api_url = model_deployed_url

    payload = {
        "inputs": inputs,
        "options": parameters
    }

    response = requests.post(api_url, json=payload, headers={"Authorization": f"Bearer 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"})
    return response.json()
