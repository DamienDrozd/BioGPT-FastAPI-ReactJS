from fastapi import FastAPI
from models import SentenceModel
from db import db
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from transformer import transform_text


app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:8080",
    "http://localhost:3000"
]


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/note")
async def add_note(new_note: str):
    phrase = transform_text(new_note)
    new_sentence = SentenceModel(note=new_note, phrase=phrase)
    sentence = await db["sentence"].insert_one(dict(new_sentence))
    response = {"suggest": phrase}
    return JSONResponse(content=response)


@app.get("/note")
async def get_note(new_note: str):
    phrase = transform_text(new_note)
    print(phrase)
    return JSONResponse(content=phrase)
