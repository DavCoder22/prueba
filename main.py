from fastapi import FastAPI
from pydantic import BaseModel
import openai

app = FastAPI()

# Contraseñas para OpenAI
openai.organization = 'org-BdVu8mIjZAXo0lZwnmNxSj7v'
openai.api_key = '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'

class Document(BaseModel):
    item: str = 'pizza'

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}

@app.post("/inference", status_code=200)
def inference(doc: Document):
    ingredientes = process_inference(doc.item)
    return {
        'response': ingredientes
    }

@app.post("/inference", status_code=200)
def process_inference(user_prompt) -> str:
    print('[PROCESANDO]'.center(40, '-'))
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "profesor de programación"},
            {"role": "user", "content": user_prompt}
        ]
    )
    response = completion.choices[0].message.content["text"]
    return response

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8888)
