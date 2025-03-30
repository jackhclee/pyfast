from fastapi import FastAPI
from pyfast.db import repo
import logging
import time

logging.Formatter.converter = time.gmtime
logging.basicConfig(style="{", format="{asctime}.{msecs:03.0f}Z {levelname} [{processName}] [{threadName}] {name} {message} [{filename}:{lineno}]", datefmt="%Y-%m-%dT%H:%M:%S", level=logging.INFO)

app = FastAPI()

@app.get("/")
async def m():
  logging.info(f"called def")
  return f"Hello World!!!!!!++ {time.gmtime()} {repo.get_record(99)} {repo.get_all_record()}"
