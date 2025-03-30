from fastapi import FastAPI
from pyfast.db import repo
import time

app = FastAPI()

@app.get("/")
async def m():
  print(dir(repo))
  return f"Hello World!!!!!!++ {time.gmtime()} {repo.get_record(99)} {repo.get_all_record()}"
