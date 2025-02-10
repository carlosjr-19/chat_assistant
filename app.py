from openai import OpenAI
from dotenv import load_dotenv, find_dotenv
import os

load_dotenv(find_dotenv())

SECRET_KEY = os.getenv("API_KEY_OR")

client = OpenAI(api_key=SECRET_KEY, base_url="https://openrouter.ai/api/v1")

pregunta = ""

while pregunta != "exit":

    pregunta = input("\n\nCon que puedo ayudarte? \n")

    response = client.chat.completions.create(
        model="deepseek/deepseek-r1:free",
        messages=[
            {"role": "system", "content": "You are a helpful assistant"},
            {"role": "user", "content": pregunta},
        ],
    )

    print(response.choices[0].message.content)    