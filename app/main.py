from fastapi import FastAPI

app = FastAPI(
    title="Campus Maintenance Resolution Agent",
    version="0.1.0",
)

@app.get("/")
def home() -> dict[str, str]:
    return {"message": "Campus Maintenance Resolution Agent API is running"}

@app.get("/health")
def health_check() -> dict[str, str]:
    return {"status": "healthy"}
