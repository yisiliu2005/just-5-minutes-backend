from dotenv import load_dotenv
import os
from flask import Flask
from flask import request
from markupsafe import escape
from google import genai

load_dotenv()

app = Flask(__name__)

# The client gets the API key from the environment variable `GEMINI_API_KEY`.
client = genai.Client()


#Flask:

@app.route("/hello")
def hello_world():
    name = request.args.get("name", "User")
    return f"Hello, {escape(name)}!"


@app.route("/user/<username>")
def getUser(username):
    return f"Hello, {escape(username)}!"


#Gemini API:
response = client.models.generate_content(
    model="gemini-2.5-flash", contents="Explain how AI works in a few words"
)
print(response.text)



