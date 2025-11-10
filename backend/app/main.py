from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.db.base import Base
from app.db.session import engine
from app.api.endpoints import auth, schedule, utils
from app.initial_data import create_first_superuser

Base.metadata.create_all(bind=engine)

create_first_superuser()

app = FastAPI(title="Вузуслуги API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router, prefix="/api/auth", tags=["Auth"])
app.include_router(schedule.router, prefix="/api/schedule", tags=["Schedule"])
app.include_router(utils.router, prefix="/api/utils", tags=["Utils"])


@app.get("/")
def read_root():
    return {"message": "Welcome to Vuzuslugi API"}
