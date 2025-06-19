import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Get DATABASE_URL from environment variable
DATABASE_URL = os.getenv("DATABASE_URL")

if not DATABASE_URL:
    raise ValueError("DATABASE_URL environment variable is not set")

print(f"Connecting to database: {DATABASE_URL.split('@')[1].split('/')[0] if '@' in DATABASE_URL else 'unknown'}...")  # Log host for debugging

# Create engine with proper configuration for production
engine = create_engine(
    DATABASE_URL,
    echo=True,
    pool_pre_ping=True,  # Validate connections before use
    pool_recycle=300,    # Recycle connections every 5 minutes
    connect_args={"sslmode": "require"}
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()