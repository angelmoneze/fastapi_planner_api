from fastapi import FastAPI
from routes.users import user_router
from routes.events import event_router
from fastapi.responses import RedirectResponse
from database.connection import conn
import uvicorn


#Création de l'instance FastAPI 
app = FastAPI()

#enregistrement des routes
app.include_router(user_router, prefix="/user")
app.include_router(event_router, prefix="/event")

#Création d'une base de données lors du démarrage
@app.on_event("startup")
def on_startup():
    conn()

@app.get("/")
async def home():
    return RedirectResponse(url="/event/")

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8080, reload=True)
