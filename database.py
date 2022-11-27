from sqlalchemy.orm import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine(
        "postgresql://postgres:mamacantik20@localhost/db_ristek22_oc_project",
        echo = True
)

Base = declarative_base()

SessionLocal = sessionmaker(bind=engine)