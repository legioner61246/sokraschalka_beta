import string
import random
from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse, FileResponse, RedirectResponse
from pydantic import BaseModel
app = FastAPI(title="Sokraschalka Beta")
db = {}
class URLRequest(BaseModel):
    url: str
def generate_short_key(length: int = 6) -> str:
    chars = string.ascii_letters + string.digits
    return ''.join(random.choice(chars) for _ in range(length))
@app.get("/", response_class=HTMLResponse)
async def read_root():
    return FileResponse("indekx.html")
@app.post("/shorten")
async def shorten_url(request: URLRequest):
    target_url = request.url.strip()
    if not target_url.startswith("http://") and not target_url.startswith("https://"):
        target_url = "https://" + target_url
    short_key = generate_short_key()
    while short_key in db:
        short_key = generate_short_key()
    db[short_key] = target_url
    return {"short_key": short_key}
@app.get("/{short_key}")
async def redirect_to_url(short_key: str):
    if short_key == "favicon.ico":
        raise HTTPException(status_code=444)
    target_url = db.get(short_key)
    if not target_url:
        raise HTTPException(status_code=404, detail="Ссылка не найдена")
    return RedirectResponse(url=target_url, status_code=307)