import fastapi
import uvicorn

app = fastapi.FastAPI()


@app.get("/")
def index():
    return {"message": "Hello, World"}


uvicorn.run(app)