import uvicorn
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import os
from dotenv import load_dotenv
load_dotenv()

from langchain.llms import GooglePalm

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins = ['*'],
    allow_credentials = True,
    allow_methods = ['*'],
    allow_headers = ['*']
)

@app.get('/')
async def hello():
    return {'hi': 'world'}

@app.get("/hello")
async def index():
    llm = GooglePalm(google_api_key=os.environ['GOOGLE_API_KEY'], temperature=0.2)
    ans = llm("what is 1 + 1 ?")
    print(ans)
    return {'hello': ans}


if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)