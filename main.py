import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


os.environ["NLS_LANG"] = "SWEDISH_SWEDEN.UTF8"


app = FastAPI(
    version="1.0.0"
)
origins = [
    "*",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/api")
async def root():
    return {
        'statusCode': 200,
        'headers': {
            'Access-Control-Allow-Headers': 'Content-Type',
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'OPTIONS,POST,GET'
        },
        'body': {'message': "Hello World"}
    }


@app.get("/api/test")
async def gettest():
    return {
        'statusCode': 200,
        'headers': {
            'Access-Control-Allow-Headers': 'Content-Type',
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'OPTIONS,POST,GET'
        },
        'body': {'message': "Test Done"}
    }