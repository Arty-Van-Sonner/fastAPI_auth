import os
import sys

import uvicorn

sys.path.insert(1, os.path.join(sys.path[0], '..'))
root_path = os.path.abspath(os.path.join(os.getcwd(), '..'))
if root_path not in sys.path:
    sys.path.insert(0, root_path)

from fastapi import FastAPI

from src.auth.router import router as auth_router

app = FastAPI()
app.include_router(auth_router)

if __name__ == '__main__':
    uvicorn.run('main:app', reload=True)