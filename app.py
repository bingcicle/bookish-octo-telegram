from fastapi import FastAPI
from pydantic import BaseModel, Field
from typing import Optional
import csv, time, os

app = FastAPI(title="Funding Webhook Simulator")
CSV_PATH = os.environ.get("CSV_PATH", "events.csv")

class FundingEvent(BaseModel):
    exchange: str = Field(..., examples=["mexc","bybit"])
    symbol: str
    funding_rate: float
    interval_h: float = 8
    price: Optional[float] = None
    ts: Optional[int] = None

def append_csv(row: dict):
    file_exists = os.path.exists(CSV_PATH)
    with open(CSV_PATH, "a", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=row.keys())
        if not file_exists:
            w.writeheader()
        w.writerow(row)

@app.post("/webhook")
async def webhook(ev: FundingEvent):
    row = ev.model_dump()
    row["received_at"] = int(time.time())
    append_csv(row)
    return {"ok": True, "saved": row}

@app.get("/")
async def root():
    return {"ok": True, "usage": "POST /webhook with FundingEvent JSON"}
