from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

# write

POSTGRESQL_DATABASE_URL = "postgresql://postgres:password@db/crud"

engine = create_engine(POSTGRESQL_DATABASE_URL, echo=True)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

Base = declarative_base()

# DB - 2 - Read

POSTGRESQL_DATABASE_URL = "postgresql://postgres:password@db/crud"

engine = create_engine(POSTGRESQL_DATABASE_URL, echo=True)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db2():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

Base2 = declarative_base()