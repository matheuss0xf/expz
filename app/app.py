# FastAPI + psycopg2 ou asyncpg + plain/raw SQL
# 🐘Postgres
# 🟩Nginx
from fastapi import FastAPI

from app.routes import auth, users

app = FastAPI()

app.include_router(users.router)
app.include_router(auth.router)
