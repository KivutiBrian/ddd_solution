from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# database setup
from configs.config_sqlalchemy import SessionLocal, engine, Base

# models

# create or delete tables
Base.metadata.create_all(bind=engine)
# Base.metadata.drop_all(bind=engine)

# configs
from configs.config_base import settings
# routes



app = FastAPI(
    title='DDD SHOP API',
    description='API endpoints for DDD-SHOP',
    version="0.1.0",
    redoc_url='/',
)

# setup the origins
origins = ["http://localhost","http://localhost:3000","http://127.0.0.1"]

# add the middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# include routers
# app.include_router(roles.router)