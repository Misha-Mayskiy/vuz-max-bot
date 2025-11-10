from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.db.base_class import Base
from app.db.session import engine
from app.api.endpoints import auth, schedule, utils, superadmin, universityadmin
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
app.include_router(superadmin.router, prefix="/api/superadmin", tags=["Super Admin"])
app.include_router(universityadmin.router, prefix="/api/university", tags=["University Admin"])
app.include_router(schedule.router, prefix="/api/schedule", tags=["Schedule Management"])
app.include_router(utils.router, prefix="/api/utils", tags=["Data Retrieval"])


@app.get("/")
def read_root():
    return {"message": "Welcome to Vuzuslugi API"}
