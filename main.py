from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from models import Law, Lawcontents, Revision, Bgbl, Base
from schemas import LawCreate, Law, Lawcontents, Revision, Bgbl
from typing import List
import models

SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base.metadata.create_all(bind=engine)

app = FastAPI()

# Accept ALL Origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/laws/", response_model=Law)
async def create_law(law: LawCreate, db: Session = Depends(get_db)):
    db_law = models.Law(**law.dict())
    db.add(db_law)
    db.commit()
    db.refresh(db_law)
    return db_law

@app.post ("/lawcontents/", response_model=Lawcontents)
async def create_lawcontents(lawcontents: Lawcontents, db: Session = Depends(get_db)):
    db_lawcontents = models.Lawcontents(**lawcontents.dict())
    db.add(db_lawcontents)
    db.commit()
    db.refresh(db_lawcontents)
    return db_lawcontents

# Get all laws (id, title and date)
@app.get("/laws/", response_model=List[Law])
def list_laws(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    laws = db.query(models.Law).offset(skip).limit(limit).all()
    return laws

# Get lawcontents by lawid
@app.get("/lawcontents/{lawid}", response_model=List[Lawcontents])
def get_lawcontents(lawid: int, db: Session = Depends(get_db)):
    lawcontents = db.query(models.Lawcontents).filter(models.Lawcontents.lawid == lawid).all()
    return lawcontents

# Serve index.html from main directory
app.mount("/", StaticFiles(directory="static", html=True), name="static")
