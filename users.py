from fastapi import APIRouter
from models.users import User
from models.users import users
from dotenv import load_dotenv
from os import environ

load_dotenv()

router = APIRouter()

API_KEY = environ.get("SECRET_KEY")


@router.get("/")
async def get_users_name(apikey:str):
    if apikey == API_KEY:
        ls=[]
        for i in users:
            ls.append(i.name())
        return ls
    return {"error":"no access to this page"}
@router.post("/")
async def add_users(users:User,apikey:str):
    if apikey == API_KEY:
        users.append(users)
        return {users:"added"}
    return {"error":"no access to this page"}
@router.delete("/delete")
async def delete_users(name:str,apikey:str):
    if apikey == API_KEY:
        for n in users:
            if n.name() == name:
                users.remove(n)
                return {name:"delete"}
        return {"error":"not find"}
    return {"error": "no access to this page"}
