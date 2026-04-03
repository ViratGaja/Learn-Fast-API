from fastapi import FastAPI, Depends
from schemas import Todo as TodoSchema, TodoCreate
from database import SessionLocal, Base, engine
from sqlalchemy.orm import Session
from models import Todo

# Database-la intha table illana, thonthira illama create pannidum
Base.metadata.create_all(bind=engine)

app = FastAPI()

# Database Connection handle panna intha function (Dependency)
def get_db():
    db = SessionLocal() # Connection-ah open pannuthu
    try:
        yield db       # Intha connection-ah API function-ku tharuval (Provide)
    finally:
        db.close()     # Velai mudinja apram connection-ah close pannidum (Safety)

# POST Method - Pudhu Todo-va create panna
@app.post("/todos", response_model=TodoSchema)
def create(todo: TodoCreate, db: Session = Depends(get_db)):
     
     # Pydantic Schema data-va (JSON) SQL Model-ah mathuthu
     # **todo.dict() na title, description ella data-vaiyum "unpack" pannum
     db_todo = Todo(**todo.model_dump())
     
     db.add(db_todo)      # Intha data-va Database-la 'Add' pannu (Stage)
     db.commit()          # Changes-ah database-la 'Save' pannu (Finalize)
     db.refresh(db_todo)  # DB-la generate aana 'id'-ya thirumba model-ku kondu vaa
     
     return db_todo       # Create aana data-va response-ah thirumba anupu
 
 
 
 #Get
 
@app.get("/todos",response_model=list[TodoSchema])
def ready_todos(db: Session=Depends(get_db)):
    return db.query(Todo).all()



