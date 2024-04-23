from pydantic import BaseModel
from typing import List, Optional
from datetime import date

class LawBase(BaseModel):
    lawtitle: str
    lawcode: str
    verabschiedet: date

class LawCreate(LawBase):
    pass

class Law(LawBase):
    lawid: Optional[int] = None  # Make lawid optional

    class Config:
        from_attributes = True

class LawcontentsBase(BaseModel):
    section: str
    content: str
    datum: date

class LawcontentsCreate(LawcontentsBase):
    pass

class Lawcontents(LawcontentsBase):
    lawid: int

    class Config:
        from_attributes = True

class RevisionBase(BaseModel):
    section: str
    operator: str
    content: str
    datum: date
    bgblid: Optional[str]
    bgblfundstelle: Optional[str]

class RevisionCreate(RevisionBase):
    pass

class Revision(RevisionBase):
    lawid: int

    class Config:
        from_attributes = True

class BgblBase(BaseModel):
    bgbldate: date
    bgblcontent: str
    bgblpath: str

class BgblCreate(BgblBase):
    pass

class Bgbl(BgblBase):
    bgblid: str

    class Config:
        from_attributes = True
