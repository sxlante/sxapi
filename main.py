from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles # Bunu ekledik
from fastapi.responses import HTMLResponse

app = FastAPI()

# KRİTİK NOKTA: Uygulamanın olduğu ana dizini statik dosyalara açıyoruz
# Eğer dosyaların 'static' diye bir klasördeyse orayı gösteririz
# Ama senin dosyaların ana dizindeyse böyle yapabiliriz:
app.mount("/static", StaticFiles(directory="."), name="static")

@app.get("/", response_class=HTMLResponse)
async def read_index():
    with open("index.html", "r", encoding="utf-8") as f:
        return f.read()

@app.get("/api/")
def test():
    return {"test": "runing"}