import uuid

from fastapi import APIRouter, Depends, HTTPException, Form, Body
from sqlalchemy.orm import Session
from typing import Optional, List
# dependency
from configs.config_sqlalchemy import get_db
# schema
from schema import store_schema
# service

# util
from util.security import *

# router object
router = APIRouter(
    prefix="/stores",
    tags=["STORE"],
    responses={
        200:{'description':'Ok'},
        201:{'description':'created'},
        400: {"description": "Bad Request"},
        404: {"description": "Not found"}
    } 
)

@router.get('',
summary='get a list of all stores',
response_model=List[store_schema.Store],
response_description="list of all stores",
status_code=200
)
async def fetch_stores(

):
    return