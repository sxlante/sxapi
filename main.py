from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles # İleride resim/css eklersen lazım olur

app = FastAPI()

# Ana sayfaya (/) girildiğinde index.html dosyasını gönderir
@app.get("/")
def ana_sayfa():
    return FileResponse("index.html")

@app.get("/.well-known/discord")
def dc_dogrulama():
    return "dh=83c3b01a0d3112bb962651a1cde20350bffb5032"
 
@app.get("/api/v1/selam")
def selam_api():
    return {
        "durum": "basarili",
        "mesaj": "Vercel üzerinden selamlar!",
        "versiyon": "1.0"
    }