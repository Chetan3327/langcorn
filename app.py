from langcorn import create_service
from fastapi.middleware.cors import CORSMiddleware

app = create_service(
    'llm_chain:chain',
    'conversation_chain:conversation'
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
