from fastapi import APIRouter, Body, HTTPException, status
from models.events import Event
from typing import List

event_router = APIRouter(
    tags=["Events"]
)

events = []

#route pour récupérer tous les évènements
@event_router.get("/", response_model=List[Event])
async def retrieve_all_events() -> List[Event]:
    return events


#route pour récupérer un seul élément
@event_router.get("/{id}", response_model=Event)
async def retrieve_event(id: int) -> Event:
    for event in events:
        if event.id == id:
            return event
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Il n'existe aucun évènement avec cet ID"
    )


#route pour créer un nouvel évènement
@event_router.post("/new")
async def create_event(body: Event = Body(...)) -> dict:
    events.append(body)
    return{
        "message": "Evènement créé avec succès"
    }


#route pour supprimer un évènement
@event_router.delete("/{id}")
async def delete_event(id: int) -> dict:
    for event in events:
        if event.id == id:
            events.remove(event)
            return {
                "message": "Evènement supprimé avec succès"
            }
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Il n'existe aucun évènement avec cet ID"
    )


#route pour supprimer tous les évènements
@event_router.delete("/")
async def delete_all_events() -> dict:
    events.clear()
    return {
        "message": "Tous les évènements ont été supprimé avec succès"
    }