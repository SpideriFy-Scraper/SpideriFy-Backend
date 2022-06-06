from typing import Union
from pydantic import BaseModel
from fastapi import FastAPI
from typing import Optional
from typing import List
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()



class ReqSen(BaseModel):
    signature_name:Optional[str]
    instances : Optional[List[str]]

class ResSen(BaseModel):
    predictions: Optional[List[List[float]]]


class SummarizationRequest(BaseModel):
    text: str


class SummarizationResponse(BaseModel):
    summarized_text: str


origins = [
    "http://spiderify-api:8080",
    "http://spiderify-api",
    "http://localhost",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post(
    "/v1/models/sentiment",
    response_model=ResSen
    )
async def read_item(
    req: ReqSen
):
    return {
        "predictions": [[-6.53907] for i in range(len(req.instances))]
        }


@app.post("/predict", response_model=SummarizationResponse)
def predict(
    request: SummarizationRequest,
    ):
    return {"summarized_text": "Fuck U"}
