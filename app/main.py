from fastapi import FastAPI
from app.routes import router

app = FastAPI(title="ContextifyAI")

app.include_router(router)