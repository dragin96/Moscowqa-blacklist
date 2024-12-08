from fastapi import FastAPI
from features.blacklist.infrastructure.web.api import router as blacklist_router
from infrastructure.database.session import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(blacklist_router)