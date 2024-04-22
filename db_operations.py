from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from datetime import date
from models import Base, law, fullfetch, Revision, bgbl

engine = create_engine('sqlite:///law.db')
Session = sessionmaker(bind=engine)
session = Session()

# Hinzufügen eines neuen Gesetzestitels. Der Code ist der Kurzname des Gesetzes, z.B. "BGB" für das Bürgerliche Gesetzbuch.
def add_law(title, code, verabschiedet):
    new_law = law(lawtitle=title, lawcode=code, verabschiedet=verabschiedet)
    session.add(new_law)
    session.commit()

# Hinzufügen eines neuen Abschnitts zu einem Gesetz (Volltext).
# Das Datum ist das Datum des Gesetzes-Fetches.
def add_section(law_id, section, content, datum):
    new_section = fullfetch(lawid=law_id, section=section, content=content, datum=datum)
    session.add(new_section)
    session.commit()

# Funktion zum Hinzufügen einer Revision.
# Der Operator ist die Handlung, die durchgeführt wurde, z.B. "Add", "Delete", "Change".
# Das Datum ist das Datum der Revision.
# Die BGBl-ID ist die ID des Bundesgesetzblatts, in dem die Revision veröffentlicht wurde.
# Die BGBl-Fundstelle ist die genaue Fundstelle im Bundesgesetzblatt (z.B. S. 219 Z 13). 
def add_revision(law_id, section, operator, content, datum, bgbl_id, bgbl_fundstelle):
    new_revision = Revision(lawid=law_id, section=section, operator=operator, content=content, datum=datum, bgblid=bgbl_id, bgblfundstelle=bgbl_fundstelle)
    session.add(new_revision)
    session.commit()

# Funktion zum Hinzufügen einer AUsgabe des Bundesgesetzblatts
# Das Datum ist das Datum der Ausgabe.
# BGBLcontent enthält den Inhalt der Ausgabe.
# BGBLpath ist der Pfad zur PDF-Datei der Ausgabe
# BGBL-ID ist die ID der Ausgabe, z.B. "BGBl. I 2019"
def add_bgbl(bgbl_id, bgbl_date, bgbl_content, bgbl_path):
    new_bgbl = bgbl(bgblid=bgbl_id, bgbldate=bgbl_date, bgblcontent=bgbl_content, bgblpath=bgbl_path)
    session.add(new_bgbl)
    session.commit()

# Funktion zum Löschen eines Gesetzes anhand seiner ID
def delete_law_by_id(law_id):
    law_to_delete = session.query(law).filter_by(lawid=law_id).first()
    session.delete(law_to_delete)
    session.commit()

# Funktion zum Löschen eines Abschnitts anhand seiner ID
def delete_section_by_id(section_id):
    section_to_delete = session.query(fullfetch).filter_by(lawid=section_id).first()
    session.delete(section_to_delete)
    session.commit()

# Funktion zum Löschen einer Revision anhand ihrer ID
def delete_revision_by_id(revision_id):
    revision_to_delete = session.query(Revision).filter_by(lawid=revision_id).first()
    session.delete(revision_to_delete)
    session.commit()

# Funktion zum Löschen einer Ausgabe des Bundesgesetzblatts anhand ihrer ID
def delete_bgbl_by_id(bgbl_id):
    bgbl_to_delete = session.query(bgbl).filter_by(bgblid=bgbl_id).first()
    session.delete(bgbl_to_delete)
    session.commit()


