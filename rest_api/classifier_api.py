from fastapi import FastAPI, Request, Response, Depends, HTTPException, status ,File,Form, UploadFile
from fastapi.encoders import jsonable_encoder
from fastapi.security import HTTPBasic, HTTPBasicCredentials
import secrets
import os
from typing import Dict
import io
import pandas as pd
#from ML.config.config import log
from ML.src.classifier import train_classifier,make_predictions
import logging
logging.basicConfig(filename='ML_server.log',filemode='w', level=logging.DEBUG,format=' %(asctime)s %(levelname)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')


app = FastAPI()
security = HTTPBasic()


'''
HTTP basic authentication based on service user name , password
''' 
def basic_auth(credentials: HTTPBasicCredentials = Depends(security)):
    SERVICE_USER = os.getenv('SERVICE_USER','admin')
    SERVICE_PASS = os.getenv('SERVICE_PASS','password')

    if not SERVICE_USER:
        print('SERVICE_USER not specified.')

    if not SERVICE_PASS:
        print('SERVICE_PASS not specified. ')

    correct_username = secrets.compare_digest(credentials.username, SERVICE_USER)
    correct_password = secrets.compare_digest(credentials.password, SERVICE_PASS)
    if not (correct_username and correct_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Basic"},
        )
    return credentials.username


@app.post('/train_model')
def train_pipeline(request: Request, response: Response ,
                   username: str = Depends(basic_auth),
                csv_file: bytes = File(...), target_variable: str = Form(...)):
    logging.info('Training API is authenticated for user: '+username)
    train_df =  pd.read_csv(io.BytesIO(csv_file), encoding='utf8',index_col=None)
    try:
        logging.info('Model training is happening')
        training_msg = train_classifier(train_df,target_variable)
        result={'status':"Model training success",'code':200,'output':training_msg}  
    except:
        logging.info('Model training has failed')
        result={'status':"Model training failed",'code':400}
    return jsonable_encoder(result)


@app.post('/get_prediction')
def test_pipeline(request: Request, response: Response ,
                  username: str = Depends(basic_auth),
                csv_file: bytes = File(...), target_variable: str = Form(...) ):
    logging.info('Prediction API is authenticated for user: '+username)
    test_df =  pd.read_csv(io.BytesIO(csv_file), encoding='utf8',index_col=None)
    try:
        logging.info('Obtaining model predictions')
        testing_msg = make_predictions(test_df,target_variable)
        result={'status':"Predcitions are success",'code':200,'output':testing_msg}  
    except:
        logging.info('Obtaining model predictions has failed')
        result={'status':"Predicitons failed",'code':400}
        
    return jsonable_encoder(result)

@app.get("/")
def hello():
    """Liveness prob"""
    return "Welcome to Machine learning server!"