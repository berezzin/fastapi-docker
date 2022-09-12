import os

from fastapi import FastAPI
import uvicorn
from fastapi.routing import APIRoute, APIRouter
from motor.motor_asyncio import AsyncIOMotorClient
from starlette.requests import Request

app = FastAPI()
MONGODB_URL = os.getenv('MONGODB_URL')


async def index() -> str:
    return 'You are on the index page'


async def ping() -> dict:
    return {'Success': True}


async def create_record(request: Request):
    mongo_client: AsyncIOMotorClient = request.app.state.mongo_client['test_database']
    await mongo_client.records.insert_one({'sample': 'record'})
    return {'Success': True}


routes = [APIRoute(path='/', endpoint=index, methods=['GET']),
          APIRoute(path='/ping', endpoint=ping, methods=['GET']),
          APIRoute(path='/create_record', endpoint=create_record, methods=['POST'])]

client = AsyncIOMotorClient(MONGODB_URL)
app.state.mongo_client = client
app.include_router(APIRouter(routes=routes))

if __name__ == '__main__':
    uvicorn.run(app=app, host='0.0.0.0', port=8000)
