from fastapi import FastAPI
from starlette.responses import Response, JSONResponse

app = FastAPI()

@app.get("/")
def read_root():
    return JSONResponse(
        content={"message": "API is running"},
        status_code=200,
        media_type="application/json"
    )

@app.get("/favicon.ico")
def favicon():
    return Response(status_code=204)  # = No Content
