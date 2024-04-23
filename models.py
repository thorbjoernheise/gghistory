# models.py
from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Law(Base):
    __tablename__ = 'law'
    lawid = Column(Integer, primary_key=True, autoincrement=True)
    lawtitle = Column(String)
    lawcode = Column(String)
    verabschiedet = Column(Date)

class Lawcontents(Base):
    __tablename__ = 'Lawcontents'
    lawid = Column(Integer, ForeignKey('law.lawid'), primary_key=True)
    section = Column(String)
    content = Column(String)
    datum = Column(Date)
    law = relationship("Law")

class Revision(Base):
    __tablename__ = 'revisionen'
    lawid = Column(Integer, ForeignKey('law.lawid'), primary_key=True)
    section = Column(String)
    operator = Column(String)
    content = Column(String)
    datum = Column(Date)
    bgblid = Column(String, ForeignKey('bgbl.bgblid'))
    law = relationship("Law")
    bgbl = relationship("Bgbl")
    bgblfundstelle = Column(String)

class Bgbl(Base):
    __tablename__ = 'bgbl'
    bgblid = Column(String, primary_key=True)
    bgbldate = Column(Date)
    bgblcontent = Column(String)
    bgblpath = Column(String)
