# Ollama: Math-or-Ping Model (assessment)

## Files
- `Modelfile` — custom model spec + SYSTEM prompt.
- `demo.py` — Python demo script that queries the model.
- `Dockerfile` & `docker-compose.yml` — optional containerized setup.

## Docker / Docker Compose
1. `docker compose up -d ollama`
2. `docker compose exec ollama ollama create mymath -f /models/Modelfile`
3. `docker compose up --build demo or python3 demo.py`

## Design notes
- System prompt enforces exact responses for 3 cases: math answers (plain numeric), `ping` → `pong!!!`, otherwise refusal phrase:  
  `I am designed to only answer mathematical questions or respond to 'ping'.`
- Deterministic parameters (`temperature: 0.0`, `top_p: 0.0`, `top_k: 1`) ensure reproducible exact outputs.
