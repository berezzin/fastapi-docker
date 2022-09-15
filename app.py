import os
from typing import List

from fastapi import FastAPI
import uvicorn
from fastapi.routing import APIRoute, APIRouter
from motor.motor_asyncio import AsyncIOMotorClient
from sqlalchemy import select
from starlette.requests import Request

import schema
from models import async_session, User

app = FastAPI()
MONGODB_URL = os.getenv('MONGODB_URL')


async def index() -> str:
    return 'You are on the index page'


async def ping() -> dict:
    return {'Success': True}


async def create_pg_record(request: Request):
    async with async_session() as session:
        new_user = User(username='Ivan', work='google.com')
        session.add(new_user)
        await session.commit()
        return [new_user.id, new_user.username, new_user.work]


async def get_all_pg_record(request: Request):
    async with async_session() as session:
        query = select(User)
        result = await session.execute(query)
        users = [i for i in result.scalars().all()]
        return users


async def create_record(request: Request):
    mongo_client: AsyncIOMotorClient = request.app.state.mongo_client['test_database']
    await mongo_client.records.insert_one({'sample': 'record'})
    return {'Success': True}


routes = [APIRoute(path='/', endpoint=index, methods=['GET']),
          APIRoute(path='/ping', endpoint=ping, methods=['GET']),
          APIRoute(path='/create_record', endpoint=create_record, methods=['POST']),
          APIRoute(path='/create_pg_record', endpoint=create_pg_record, methods=['POST']),
          APIRoute(path='/get_all_pg_record',
                   endpoint=get_all_pg_record,
                   methods=['GET'],
                   response_model=List[schema.User])]

client = AsyncIOMotorClient(MONGODB_URL)
app.state.mongo_client = client
app.include_router(APIRouter(routes=routes))

if __name__ == '__main__':
    uvicorn.run(app=app, host='0.0.0.0', port=8000)
