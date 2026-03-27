from pydantic import BaseModel

class TodoBase(BaseModel):
    title: str                      # Inga 'title' kandippa string-ah irukanum (Required)
    description: str | None = None  # Idhu optional, illana 'None' (null) nu eduthukkum
    completed: bool = False         # Default-ah false-nu set aagidum (Boolean type)

# create pannum pothu use aagum
class TodoCreate(TodoBase):
    pass                             # TodoBase-la irukura ellathaiyum அப்படியே copy pannikkum (Inheritance)

# Database-la irunthu response anupum pothu use aagum
class Todo(TodoBase):
    id: int                         # Database create panna 'id' inga add aagum

    class Config:                   # Pydantic-oda special settings idhu
       from_attributes = True  # Pydantic v2 syntax         # SQLAlchemy (ORM) objects-ah direct-ah JSON-ah mathurathuku idhu romba mukkiyam