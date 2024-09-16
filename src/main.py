from fastapi import FastAPI, Request
from .operations.router import router as op_rt

app = FastAPI()


@app.get("/")
def main(request: Request):
    return {
        "Status": "200 OK",
        "Detail": "",
    }


app.include_router(op_rt)
