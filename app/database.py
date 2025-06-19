import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Hard-coded DATABASE_URL for Railway deployment
DATABASE_URL = "postgresql://neondb_owner:npg_o1l9fOGsSAVH@ep-lingering-morning-a8d52lpo-pooler.eastus2.azure.neon.tech/testdb?sslmode=require"

print("Connecting to Neon database...")  # Log for debugging

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