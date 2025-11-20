#!/usr/bin/env python3
"""
demo.py
Demonstrates the three required behaviors against an Ollama model named 'mymath'.

Pre-req:
1. Create the model (on the host where Ollama is running):
   ollama create mymath -f /path/to/Modelfile

2. Start ollama server: ollama serve  (or run the docker container that exposes port 11434)

This script will call the Ollama HTTP API /api/generate.
"""

import requests
import json

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL_NAME = "mymath"  # The name you used with `ollama create mymath -f Modelfile`

tests = [
    # Mathematical queries (2+)
    "What is 10 divided by 2?",
    "Calculate the square root of 81",

    # Ping (case-insensitive)
    "ping",
    "Ping",

    # Non-math, non-ping questions (2+)
    "Tell me a story",
    "What is the capital of France?"
]

def call_ollama(prompt: str):
    payload = {
        "model": MODEL_NAME,
        "prompt": prompt,
        "stream": False,
        "max_tokens": 64
    }

    resp = requests.post(OLLAMA_URL, json=payload)
    resp.raise_for_status()
    out = resp.json()

    if "response" in out:
        return out["response"].strip()

    return "[No response field returned]"

if __name__ == "__main__":
    for test in tests:
        print("Input:", test)
        try:
            res = call_ollama(test)
        except Exception as e:
            print("ERROR calling Ollama:", e)
            break
        # Print raw output, show exact response
        print("Output:", repr(res))
        print()
