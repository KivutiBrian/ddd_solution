import uuid

from fastapi import APIRouter, Depends, HTTPException, Form, Body
from sqlalchemy.orm import Session
from typing import Optional, List
# dependency
from configs.config_sqlalchemy import get_db
# schema
from schema import role_schema
# service

# util
from util.security import *

# router object
router = APIRouter(
    prefix="/roles",
      tags=["ROLES"],
    responses={
        200:{'description':'Ok'},
        201:{'description':'created'},
        400: {"description": "Bad Request"},
        404: {"description": "Not found"}
    } 
)

# GET A LIST OF ALL ROLES
@router.get('',
summary='get a list of all roles',
response_model=List[role_schema.Role],
response_description="list of all users",
status_code=200, 
)
async def get_roles(
    db:Session = Depends(get_db)
):
    return 


"""GET A ROLE BY id"""
@router.get('/{id}',
summary='get role details that matches the roleId provided',
response_model=role_schema.Role,
response_description="list of all roles",
status_code=200,
# dependencies=[Depends(karibu_admin)]
)
async def get_role(
    role_Id:int,
    db:Session=Depends(get_db), 
    current_user: attendant_schema.Attendant = Depends(get_current_active_user)
):
    return 

""""CREATE A ROLE"""
@router.post('',
summary='create a new role',
response_model=role_schema.Role,
response_description="list of all roles",
status_code=200,
# dependencies=[Depends(karibu_admin)]
)
async def create_role(
    role: role_schema.RoleBase, 
    db:Session=Depends(get_db)
):
    return 


