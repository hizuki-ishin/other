from fastapi import FastAPI, Body
from fastapi.logger import logger
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Any, Dict, List
from dateutil.relativedelta import *
import numpy as np
import random
from datetime import datetime
import dateutil


app = FastAPI()

origins = [
    "http://localhost:8888/index.html",
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def home():
    return {"health": "ok"}


@app.get("/future")
def future():

    base_date = 202204
    data_num = 12*4

    date = datetime.strptime(str(base_date), "%Y%m")
    dates = [(date - relativedelta(months=12*4 - i)) for i in range(data_num)]
    date_series = [d.strftime("%Y-%m-%d") for d in dates]

    actual_series = np.random.randint(50, 300, data_num)
    predict_series = np.random.randint(40, 350, data_num)
    diff_series = actual_series - predict_series

    response = {
        "baseDate": base_date,
        "c": "1",
        "i": "2",
        "dateSeries": date_series,
        "actualSeries": actual_series.tolist(),
        "predictSeries": predict_series.tolist(),
        "diffSeries": diff_series.tolist()
    }
    return response
