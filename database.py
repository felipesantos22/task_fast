import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

#Postgress
#DATABASE_URL = "postgresql+psycopg2://postgres:postgres@localhost:5432/dbtask"

#SQLite
#DATABASE_URL = "sqlite:///database.db"

#MySql
#DATABASE_URL = "mysql+pymysql://root:123456@localhost:3306/dbtask"
#28/03
database_url = os.getenv("MYSQL_PUBLIC_URL")

if database_url and database_url.startswith("mysql://"):
    database_url = database_url.replace("mysql://", "mysql+pymysql://", 1)

if not database_url:
    database_url = "mysql+pymysql://root@localhost:3306/dbtask"

engine = create_engine(database_url, echo=True)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

