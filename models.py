from sqlalchemy import Column, Integer, String, Date, create_engine, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class law(Base):
    __tablename__ = 'law'
    lawid = Column(Integer, primary_key=True)
    lawtitle = Column(String)
    lawcode = Column(String)
    verabschiedet = Column(Date)
    

class fullfetch(Base):
    __tablename__ = 'fullfetch'
    lawid = Column(Integer, ForeignKey('law.lawid'), primary_key=True)
    section = Column(String)
    content = Column(String)
    datum = Column(Date)
    law = relationship("law")


class Revision(Base):
    __tablename__ = 'revisionen'
    lawid = Column(Integer, ForeignKey('law.lawid'), primary_key=True)
    section = Column(String)
    operator = Column(String)
    content = Column(String)
    datum = Column(Date)
    bgblid = Column(String, ForeignKey('bgbl.bgblid'))
    law = relationship("law")
    bgbl = relationship("bgbl")
    bgblfundstelle = Column(String)

class bgbl(Base):
    __tablename__ = 'bgbl'
    bgblid = Column(String, primary_key=True)
    bgbldate = Column(Date)
    bgblcontent = Column(String)
    bgblpath = Column(String)


# Erstellen Sie eine SQLite-Datenbank und eine Sitzung
engine = create_engine('sqlite:///law.db')
Session = sessionmaker(bind=engine)

# Erstellen Sie die Tabellen
Base.metadata.create_all(engine)