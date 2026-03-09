@app.post("/chat")
async def chat(user_message: str):
    return {"response": "AI health advice will appear here"}
