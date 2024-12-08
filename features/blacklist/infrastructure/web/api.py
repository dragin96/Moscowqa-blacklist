from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from infrastructure.database.session import get_db
from features.blacklist.domain.services import BlacklistService
from features.blacklist.domain.models import BlacklistUser
from features.blacklist.infrastructure.database.repositories import SQLAlchemyBlacklistRepository


router = APIRouter()

def get_blacklist_service(db: Session = Depends(get_db)):
    repository = SQLAlchemyBlacklistRepository(db)
    return BlacklistService(repository)

@router.post("/blacklist")
def add_user(user: BlacklistUser, service: BlacklistService = Depends(get_blacklist_service)):
    service.add_user_to_blacklist(user)
    return {"message": "User added to blacklist"}

@router.get("/blacklist/{user_id}")
def get_user(user_id: int, service: BlacklistService = Depends(get_blacklist_service)):
    return service.get_user(user_id)

@router.get("/blacklist")
def get_all_users(service: BlacklistService = Depends(get_blacklist_service)):
    return service.get_all_users()

@router.delete("/blacklist/{user_id}")
def delete_user(user_id: int, service: BlacklistService = Depends(get_blacklist_service)):
    service.remove_user(user_id)
    return {"message": "User removed from blacklist"}
