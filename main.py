from fastapi import FastAPI
import uvicorn
from utlity_functions import remove_vowels, letter_counts_map, remove_every_third, reverse_str, to_upper
import json

app = FastAPI()


@app.get("/reverse")
def return_reverce(s: str):
    reversed = reverse_str(s)
    ready_for_json = { "original": s, "reversed_text": reversed }
    return ready_for_json




