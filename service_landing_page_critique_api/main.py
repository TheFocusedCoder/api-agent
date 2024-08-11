import os
from fastapi import FastAPI, HTTPException
from modal import Image, Secret, asgi_app
import modal
import requests
from bs4 import BeautifulSoup
from openai import OpenAI

web_app = FastAPI()
app = modal.App("landing-page-critique-api")

image = Image.debian_slim().pip_install("beautifulsoup4", "requests", "openai")

@web_app.post("/analyze")
async def analyze_landing_page(body: dict):
    try:
        url = body["url"]
        # Scrape the landing page
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        text_content = soup.get_text()

        # Analyze the content using GPT-4
        client = OpenAI()
        completion = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a copywriting expert. Analyze the following landing page content and provide a critique."},
                {"role": "user", "content": text_content}
            ]
        )

        review = completion.choices[0].message.content

        return {"review": review}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.function(image=image, secrets=[Secret.from_name("OPENAI_API_KEY")])
@asgi_app()
def fastapi_app():
    return web_app

