from fastapi import APIRouter,Depends,Request
from fastapi.responses import JSONResponse,HTMLResponse
from ..database import Base,get_db,Base2,get_db2
from sqlalchemy.orm import Session
from ..schemas import Users,Users_Out
from ..models import Users as Users_model
from sqlalchemy.exc import IntegrityError
from typing import List

router = APIRouter()


@router.post("/users",response_model=Users)
def add_User(data : Users , db: Session = Depends(get_db)):
    try:
        datas = Users_model(username = data.username , password = data.password)
        db.add(datas)
        db.commit()
        db.refresh(datas)
        return datas
    
    except Exception as e:
        return JSONResponse(content={"msg":e},status_code=500)
    
@router.get("/users",response_model=List[Users_Out])
def get_User(db: Session = Depends(get_db2)):
        return db.query(Users_model).all()