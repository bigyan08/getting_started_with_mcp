import requests

def call_llm(prompt: str):
    data = {
        "model": "llama3",
        "messages": [{"role": "user", "content": prompt}],
        "stream":False
    }
    resp = requests.post("http://localhost:11434/api/chat", json=data)
    resp.raise_for_status() #check for errors
    return resp.json()["message"]["content"]
