from fastapi import FastAPI


app = FastAPI()

@app.get("/greeting")
def hi():
    return {"respond": "Привіт з сервера2"}