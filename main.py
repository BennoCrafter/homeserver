from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from app.routes.observice.observice import observice_router

app = FastAPI()

# Observice
app.include_router(observice_router, prefix="/observice", tags=["observice"])
app.mount("/static", StaticFiles(directory="app/routes/observice/static"), name="observice_static")

@app.get("/")
def read_root():
    return {"message": "Welcome to the Home Server app!"}
