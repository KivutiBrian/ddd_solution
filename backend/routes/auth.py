import uuid

from fastapi import APIRouter, Depends, HTTPException, Form, Body
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

# dependency
from configs.config_sqlalchemy import get_db
# schema
from schema import store_schema 



# define the url the client will use to access the token
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/login")

# router object
router = APIRouter(
    prefix="/auth",
      tags=["AUTHORIZATION AND AUTHENTICATION"],
    responses={
        200:{'description':'Ok'},
        201:{'description':'created'},
        400: {"description": "Bad Request"},
        404: {"description": "Not found"}
    } 
)

# register a new account
@router.post("/account/register",
summary='register to create a new store',
response_model=store_schema.Store,
status_code=201
)
async def account_register(
    StoreName: str = Body(...),
    OwnerFirstName: str = Body(...),
    OwnerLastName: str = Body(...),
    OwnerEmail: str = Body(...),
):
    return
    
# account login
@router.post('/login',
summary='login to get access token',
status_code=200
)
async def login(form_data: OAuth2PasswordRequestForm = Depends(), db:Session=Depends(get_db)):
    user = authenticate_user(email=form_data.username, password=form_data.password, db=db)
    if not user:
        raise HTTPException(
            status_code=401,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": str(user.id)}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer", "user":user}
