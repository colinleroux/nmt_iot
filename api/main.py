import casbin
from fastapi import FastAPI
from fastapi_authz import CasbinMiddleware
from starlette.middleware.authentication import AuthenticationMiddleware

import basic_auth
app = FastAPI()
enforcer = casbin.Enforcer(
   'rbac_model.conf',
   'rbac_policy.csv',
)
backend = basic_auth.BasicAuth()

app.add_middleware(CasbinMiddleware, enforcer=enforcer)
app.add_middleware(AuthenticationMiddleware, backend=backend)


@app.get("/")
async def index():
   return {"message": "Hello World"}

@app.get("/ds1/res1")
async def ds1_res1():
    return "Greetings from the ds1/res1 endpoint"

@app.get("/ds2/res2")
async def ds2_res2():
    return "Helloa from the ds2/res2 endpoint"