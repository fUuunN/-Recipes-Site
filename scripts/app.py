from fastapi import FastAPI
from response import recipe_response
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],  
    allow_headers=["*"],  
)


@app.get("/chatbot")
async def chat_with_bot_get(user_input: str):
    response = recipe_response(user_input)
    return {"message": response}
