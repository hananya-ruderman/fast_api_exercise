import uvicorn
from string_ops import remove_vowels, letter_counts_map, remove_every_third, reverse_str, to_upper
import json
from fastapi import FastAPI

app = FastAPI()

@app.get("/reverse")
def return_reverce(s: str):
    reversed = reverse_str(s)
    ready_for_json = { "original": s, "reversed_text": reversed }
    return ready_for_json


@app.get("/uppercase/{text}")
def to_uppers(text: str):
    upper_str = to_upper(text)
    x = { "original": text, "uppercased": upper_str }
    return x

@app.post("/remove-vowels")
def remove_vowels_from_str(file_json: dict):
    with open ("file.json","r") as f:
      data = json.load(f)
    new_data = remove_vowels(data)
    data_collection = data.append(new_data)
    with open ("file.json","w") as f:
       json.dump(data_collection)


if __name__ == "__main__":
    pass