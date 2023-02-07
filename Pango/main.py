from fastapi import FastAPI
import uvicorn

from app.resources.routes import api_router

app = FastAPI()
app.include_router(api_router)

if __name__ == "__main__":
    try:
        uvicorn.run(app, host="0.0.0.0")
    except Exception as ex:
        print(f'application failed to start')