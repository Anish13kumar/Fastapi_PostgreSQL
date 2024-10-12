from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import JSONResponse
from ..database import get_master_db, get_slave_db
from sqlalchemy.orm import Session
from ..schemas import Users, Users_Out
from ..models import Users as Users_model
from sqlalchemy.exc import IntegrityError
from typing import List
import logging

router = APIRouter()

# Set up logging
logger = logging.getLogger(__name__)

@router.post("/users", response_model=Users)
def add_user(data: Users, db: Session = Depends(get_master_db)):
    try:
        # Log the DB URL for the write operation (master DB)
        db_url = str(db.bind.url)
        print(f"Writing to database: {db_url}")

        datas = Users_model(username=data.username, password=data.password)
        db.add(datas)
        db.commit()
        db.refresh(datas)
        return datas
    except IntegrityError as e:
        db.rollback()
        raise HTTPException(status_code=400, detail="User with this username already exists.")
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail="An unexpected error occurred.")


@router.get("/users", response_model=List[Users_Out])
def get_user(db: Session = Depends(get_slave_db)):
    # Log the DB URL for the read operation (slave DB)
    db_url = str(db.bind.url)
    print(f"Reading from database: {db_url}")

    return db.query(Users_model).all()
