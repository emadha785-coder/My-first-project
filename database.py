from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

URL = "sqlite:///./bookStore.db"

engine = create_engine(URL, connect_args={"check_same_thread": False}) 
# the connection brain, WHERE TO GO,

SessionLocal = sessionmaker(autoflush=False, autocommit= False,bind=engine) # For every connection to the file

Base = declarative_base()
