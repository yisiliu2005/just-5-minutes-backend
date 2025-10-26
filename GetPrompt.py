from dotenv import load_dotenv
import os
from flask import Flask, request
from google import genai
from pydantic import BaseModel


class StoreData(BaseModel):
    title: str
    startTime: str
    endTime: str

load_dotenv()

app = Flask(__name__)

client = genai.Client()
prompt = " can you give me a day plan in the form of a json file with those activities and say nothing else. also, write it as a normal text, not a code text"

@app.route("/gemini-response/", methods=['POST'])
def getGeminiResponses():
    if request.is_json:
        data = request.get_json(force=True)
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents= (str(data), " , please create a time for these habits during the day. It shold be in this format: title, startTime, endTime. Space the habits out throughout the day; do not have them right next to each other. The end time should be 5 minutes after the start time pretty princess"),
            config={
                "response_mime_type": "application/json",
                "response_schema": list[StoreData],
            },
        )
    return response.text, 200

    #curl -X POST -H "Content-Type: application/json" -d '[{"task": "find a job", "desc": "i need a job"},{"task": "do calc homework", "desc": "focus on studying derivatives"}]' http://127.0.0.1:5000/gemini-response/
    #python -m flask --app Main run --debug



