
from fastapi import FastAPI
from pydantic import BaseModel
import openai
from zabbix_api import ZabbixAPI
import os

app = FastAPI()

# Load credentials from environment variables
ZABBIX_SERVER = os.getenv("ZABBIX_SERVER")
ZABBIX_USERNAME = os.getenv("ZABBIX_USERNAME")
ZABBIX_PASSWORD = os.getenv("ZABBIX_PASSWORD")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Zabbix API setup
zabbix = ZabbixAPI(server=ZABBIX_SERVER)
zabbix.login(ZABBIX_USERNAME, ZABBIX_PASSWORD)

# OpenAI setup
openai.api_key = OPENAI_API_KEY

class UserInput(BaseModel):
    text: str

@app.get("/")
async def root():
    return {"message": "Welcome to the  Zabbix Incident Chatbot!"}

@app.post("/chat")
async def chat(user_input: UserInput):
    user_message = user_input.text

    # Example: Fetch active incidents from Zabbix
    if "active incidents" in user_message.lower():
        incidents = zabbix.trigger.get({"output": "extend", "filter": {"value": 1}})
        response = f"There are {len(incidents)} active incidents: {incidents}"
    else:
        # Use OpenAI for general responses
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": user_message}]
        ).choices[0].message.content

    return {"response": response}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
