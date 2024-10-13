from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

# Master DB - Write
POSTGRESQL_DATABASE_MASTER_URL = "postgresql://myuser:mypassword@master.db/mydb"
MASTER_ENGINE = create_engine(POSTGRESQL_DATABASE_MASTER_URL, echo=False)
MASTER_SessionLocal = sessionmaker(autocommit=False, autoflush=True, bind=MASTER_ENGINE)

# Slave DB - Read
POSTGRESQL_DATABASE_SLAVE_URL = "postgresql://myuser:mypassword@slave.db/mydb"
SLAVE_ENGINE = create_engine(POSTGRESQL_DATABASE_SLAVE_URL, echo=False,pool_size=1,max_overflow=0, pool_recycle=0, pool_pre_ping=True)
SLAVE_SessionLocal = sessionmaker(autocommit=False, autoflush=True, bind=SLAVE_ENGINE)

# Declare Base
Base = declarative_base()

# Get the Master DB session for write operations
def get_master_db():
    db = MASTER_SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Get the Slave DB session for read operations
def get_slave_db():
    db = SLAVE_SessionLocal()
    try:
        yield db
    finally:
        db.close()
