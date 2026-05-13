from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import items

app = FastAPI(
    title="FastAPI Demo",
    description="GitHub + Vercel + CI/CD demo loyihasi",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(items.router, prefix="/api/v1")


@app.get("/")
def root():
    return {"message": "FastAPI Vercel demo ishlayapti! 🚀", "status": "ok"}


@app.get("/health")
def health():
    return {"status": "healthy"}
