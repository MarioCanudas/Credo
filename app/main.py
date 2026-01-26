from fastapi import FastAPI
from schemas import Message

app = FastAPI()


@app.get(path="/", response_model=Message)
async def root() -> Message:
    return Message(title="test", body="Hello world")
