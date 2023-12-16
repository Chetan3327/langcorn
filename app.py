from langcorn import create_service
from fastapi.middleware.cors import CORSMiddleware

app = create_service(
    'llm_chain:chain',
    'conversation_chain:conversation'
)

origins = [
    "http://localhost",
    "http://localhost:3000",
    "https://codeflow-26ut.onrender.com"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
