import uvicorn
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
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
    return {'hello': 'world'}


if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)