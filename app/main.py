from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from app import models
from app.database import engine
from app.routers import router
import time
import os

app = FastAPI()

# Add startup delay for Railway
if os.getenv('RAILWAY_ENVIRONMENT'):
    time.sleep(2)

# Create tables with error handling
try:
    models.Base.metadata.create_all(bind=engine)
    print("✅ Database tables created successfully")
except Exception as e:
    print(f"❌ Error creating database tables: {e}")
    raise

templates = Jinja2Templates(directory="app/templates")

app.include_router(router)

@app.get("/", response_class=HTMLResponse)
def get_index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/health")
def health_check():
    return {"status": "healthy"}