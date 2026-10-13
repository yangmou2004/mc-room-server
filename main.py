from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "部署成功！"}

@app.get("/hello/{name}")
def say_hello(name: str):
    return {"msg": f"你好 {name}"}
