# funding-webhook-sim
Tiny FastAPI server that writes incoming JSON to CSV.

## Run
```bash
pip install -r requirements.txt
uvicorn app:app --reload --port 8000
```

## Test
```bash
curl -X POST http://127.0.0.1:8000/webhook           -H 'content-type: application/json'           -d '{"exchange":"bybit","symbol":"BTCUSDT","funding_rate":-0.12,"interval_h":8}'
```
Result saved to `events.csv`.
