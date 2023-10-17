from fastapi import FastAPI
import uvicorn


app = FastAPI()

API_keys=["alsjkdfh","oaopbweuv","upsNCipo"]

Fk_data = [
    {"name": "a", "score": 100, "age": 1},
    {"name": "b", "score": 99, "age": 2},
    {"name": "c", "score": 98, "age": 3},
    {"name": "d", "score": 97, "age": 4},
    {"name": "e", "score": 96, "age": 5},
    {"name": "f", "score": 95, "age": 6},
    {"name": "g", "score": 94, "age": 7},
    {"name": "h", "score": 93, "age": 8},
    {"name": "i", "score": 92, "age": 9},
    {"name": "j", "score": 91, "age": 10},
    {"name": "k", "score": 90, "age": 11},
    {"name": "l", "score": 89, "age": 12},
    {"name": "m", "score": 88, "age": 13},
    {"name": "n", "score": 87, "age": 14},
    {"name": "o", "score": 86, "age": 15},
    {"name": "p", "score": 85, "age": 16},
    {"name": "q", "score": 84, "age": 17},
    {"name": "r", "score": 83, "age": 18},
    {"name": "s", "score": 82, "age": 19},
    {"name": "t", "score": 81, "age": 20},
    {"name": "u", "score": 80, "age": 21},
    {"name": "v", "score": 79, "age": 22},
    {"name": "w", "score": 78, "age": 23},
    {"name": "x", "score": 77, "age": 24},
    {"name": "y", "score": 76, "age": 25},
    {"name": "z", "score": 75, "age": 26}
]
@app.get("/")
def home_route():
    return "Work"

#
# @app.get("/helper/random_number") #随机数
# def random_number_helper():
#     random_num= randint(0,100)
#     return {"number:":random_num}
@app.get("/user/ad")
async def read_user_me():
    return {"username": "the current user"}
@app.get("/user/all")
def get_all(apikey:str):
    if apikey in API_keys:
        ls = []
        for i in Fk_data:
            ls.append(i["name"])
        return ls
    return {"no server access"}
@app.get("/user/{user_id}")
def get_user(user_id: str,apikey: str):
    if apikey in API_keys:
        for i in Fk_data:
            if user_id.lower() == i["name"].lower():
                return {"user_id": user_id}
        return {"user_id": "name not found"}
    return {"no server access"}
@app.get("/user/{user_id}/score")
def get_user(user_id: str,apikey: str):
    if apikey in API_keys:
        for i in Fk_data:
            if user_id.lower() == i["name"].lower():
                return {"user_id": user_id, "score": i["score"]}
        return {"user_id": "name not found"}
    return {"no server access"}
@app.get("/user/{user_id}/age")
def get_user(user_id: str,apikey: str):
    if apikey in API_keys:
        for i in Fk_data:
            if user_id.lower() == i["name"].lower():
                return {"user_id": user_id, "age": i["age"]}
        return {"user_id": "name not found"}
    return {"no server access"}
# @app.get("/athletes/{al}")
# async def get_athlete(al:str,apikey:str):
#     if apikey in API_keys:
#

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True, host="127.0.0.1", port=8080)
