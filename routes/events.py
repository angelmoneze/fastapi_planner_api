from turtle import st
from fastapi import APIRouter, Depends, HTTPException, Request, status
from models.events import Event, EventUpdate
from sqlmodel import select
from database.connection import get_session
from typing import List

event_router = APIRouter(
    tags=["Events"]
)

events = []

#route pour récupérer tous les évènements
@event_router.get("/", response_model=List[Event])
async def retrieve_all_events(session=Depends(get_session)) -> List[Event]:
    statement = select(Event)
    events = session.exec(statement).all()
    return events


#route pour récupérer un seul élément
@event_router.get("/{id}", response_model=Event)
async def retrieve_event(id: int, session=Depends(get_session)) -> Event:
    event = session.get(Event,id)
    if event:
        return event
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Il n'existe aucun évènement avec cet ID"
    )


#route pour créer un nouvel évènement
@event_router.post("/new")
async def create_event(new_event: Event, session=Depends(get_session)) -> dict:
    session.add(new_event)
    session.commit()
    session.refresh(new_event)

    return{
        "message": "Evènement créé avec succès"
    }


#route pour supprimer un évènement
@event_router.delete("/{id}")
async def delete_event(id: int, session=Depends(get_session)) -> dict:
    event = session.get(Event, id)
    if event:
        session.delete(event)
        session.commit()
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


@event_router.put("/edit/{id}", response_model=Event)
async def update_event(id: int, new_data: EventUpdate, session=Depends(get_session)) -> Event:
    event = session.get(Event, id)
    if event:
        event_data = new_data.dict(exclude_unset=True)
        for key, value in event_data.items():
            setattr(event, key, value)
        session.add(event)
        session.commit()
        session.refresh(event)
        
        return event
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Il n'existe aucun évènement avec cet ID"
    )