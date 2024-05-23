from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return "Meu site está no ar"