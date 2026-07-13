from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import event # 👈 استيراد الأحداث


URL = "sqlite:///./bookStore.db"

engine = create_engine(URL, connect_args={"check_same_thread": False}) 
# the connection brain, WHERE TO GO,

SessionLocal = sessionmaker(autoflush=False, autocommit= False,bind=engine) # For every connection to the file

@event.listens_for(engine, "connect")
def set_sqlite_pragma(dbapi_connection, connection_record):
    cursor = dbapi_connection.cursor()
    cursor.execute("PRAGMA foreign_keys=ON")
    cursor.close()


Base = declarative_base()
