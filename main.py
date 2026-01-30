from fastapi import FastAPI
from fastapi.responses import FileResponse

app = FastAPI()

@app.get("/")
def ana_sayfa():
    return FileResponse("index.html")

@app.get("/api/selam")
def selamlama():
    return {"status": "runing", "message": "selam!", "version": "v1"}