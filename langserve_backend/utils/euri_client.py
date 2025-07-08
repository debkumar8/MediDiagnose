import requests

API_KEY = "euri-4146b0e8a2c990b6df70d149652137cf5318fcd9bf3acd97e32b3f8ab022a218"
BASE_URL = "https://api.euron.one/api/v1/euri/alpha"

def euri_chat_completion(messages, model="deepseek-r1-distill-llama-70b", temperature=0.7, max_tokens=1000):
    url = f"{BASE_URL}/chat/completions"
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    payload = {
        "model": model,
        "messages": messages,
        "temperature": temperature,
        "max_tokens": max_tokens
    }
    response = requests.post(url, headers=headers, json=payload)
    return response.json()["choices"][0]["message"]["content"]