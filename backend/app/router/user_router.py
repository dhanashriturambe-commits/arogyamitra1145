from fastapi import APIRouter
from ..schemas import UserCreate,LoginSchema
from ..auth import create_token

router = APIRouter()

fake_users=[]


@router.post("/register")
def register(user:UserCreate):

    fake_users.append(user)

    return {"message":"User Registered"}



@router.post("/login")
def login(data:LoginSchema):

    token=create_token({"user":data.email})

    return {"token":token}