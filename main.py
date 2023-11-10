from fastapi import FastAPI
import uvicorn

from routers import users

app = FastAPI()

app.include_router(users.router,prefix="/user")

if __name__=="__main__":
    uvicorn.run("main:app",reload=True)
