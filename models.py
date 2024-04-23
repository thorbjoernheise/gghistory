from sqlalchemy import Column, Integer, String, Date, ForeignKey, DateTime, func
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Law(Base):
    __tablename__ = 'law'
    lawid = Column(Integer, primary_key=True, autoincrement=True)
    lawtitle = Column(String)
    lawcode = Column(String)
    verabschiedet = Column(Date)
    timestamp = Column(DateTime, default=func.now())
    lawcontents = relationship("Lawcontents", back_populates="law")


class Lawcontents(Base):
    __tablename__ = 'lawcontents'
    lawcontentid = Column(Integer, primary_key=True, autoincrement=True)
    lawid = Column(Integer, ForeignKey('law.lawid'))
    section = Column(String)
    content = Column(String)
    datum = Column(Date)
    law = relationship("Law", back_populates="lawcontents")
    bgblid = Column(String, ForeignKey('bgbl.bgblid'))
    timestamp = Column(DateTime, default=func.now())


class Revision(Base):
    __tablename__ = 'revisionen'
    revisionid = Column(Integer, primary_key=True, autoincrement=True)
    lawid = Column(Integer, ForeignKey('law.lawid'))
    section = Column(String)
    operator = Column(String)
    content = Column(String)
    datum = Column(Date)
    bgblid = Column(String, ForeignKey('bgbl.bgblid'))
    bgblfundstelle = Column(String)
    law = relationship("Law")
    bgbl = relationship("Bgbl")
    timestamp = Column(DateTime, default=func.now())


class Bgbl(Base):
    __tablename__ = 'bgbl'
    bgblid = Column(String, primary_key=True)
    bgbldate = Column(Date)
    bgblcontent = Column(String)
    bgblpath = Column(String)
    timestamp = Column(DateTime, default=func.now())
