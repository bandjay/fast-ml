# Example scalable REST API framework for Machine Learning applications
Now a days, packaging Machine Learning applications as REST apis inside the containers has become the standard in the industry because REST apis provide great flexibility and containers offers better portability.For example you have developed machine learning classifier model in order to make it production ready we can wrap the model as a REST API inside container , this practice makes the life easier as model can be deployed, used very easily and even scaling the application is a breeze.There exists many frameworks for API development , building containers , Machine learning libraries and programming languages , however we stick to popular choices in this example i.e; Python , sci-kit learn , FastAPI , gunicorn , docker .

Below are links where you can find more info about each piece
* Python3  [ Needs no introduction ]
* sci-kit learn [ Needs no introduction ]
    More info : `https://scikit-learn.org/stable/`
* FastAPI : Webframework for building APIs, it is fast and offers high performance with asynchronous capabilities. Refer to this blog for performance comparison https://ahmed-nafies.medium.com/why-did-we-choose-fast-api-over-flask-and-django-for-our-restful-micro-services-77589534c036 
    More info : `https://fastapi.tiangolo.com/` 
* gunicorn: WSGI(Web Server Gateway Inteface) HTTP server , required to forward/manage the API requests and managing workers .It offers great compatability with FastAPI and python.
    More info : `https://docs.gunicorn.org/en/stable/`
* Uvicorn : ASGI (Asynchronous Server Gateway Interface) , required to support asynchronous requestes it complements the features offered by gunicorn with Uvicorn's performance benefits.
    More info : `https://www.uvicorn.org/`
* docker: Software to package applications its dependencies in a virtual container that can run on any Linux, Windows, or macOS computer. It offers better portability and installion for applications.
    More info : `https://www.docker.com/products/docker-app`

## Interesting pieces of the repo  
Motivation behind this repository is that most of the effort for ML application deployment is repetitive so a template for deploying ML applications using `FastAPI,gunicorn, docker` is indeed useful. In case of deploying a new ML application minimal modifications to be mage  and other dependencies installation will done automatically.

    * docker base image including python3.6,FastAPI,gunicorn at `quay.io/jaycb/fastapi-gunicorn-python3.6`
        * You don't need to install gunicorn,uvicorn,FastAPI 
    * asynchronous APIs for train and testing ML model along with basic HTTP authentication
        * Good resource to understand why asynchronous calls are required `https://realpython.com/python-async-features/`
    * Testing API on 1 million testing requests
        * Performance testing on your API to understand how much it can scale

## Pre-requisites 
* Install `docker` from `https://www.docker.com/products/docker-app` . 
        Example is tested on verison `Docker version 20.10.5, build 55c4c88`
* Install `Python 3.6.*` from `https://www.python.org/downloads/`


## Code organisation 
.
├── Dockerfile                      -   dockerfile to build ML applictaion container
├── ML                              -   directory for code related to ML application 
│   ├── __init__.py
│   ├── config                      -   configurations related to ML application
│   │   ├── __init__.py
│   │   └── config.py
│   ├── data                        -   directory for sample datasets
│   │   ├── full.csv
│   │   ├── test.csv
│   │   ├── train-test-split.py
│   │   └── train.csv
│   ├── saved_models                -   directory for saving trained model as .pkl file
│   │   └── ml_model.pkl
│   └── src                         -   directory for ML model
│       ├── __init__.py
│       └── classifier.py
├── ML_server.log                   -   Log file to capture the ML application usage and API calls
├── README.md
├── gunicorn                        -   directory for Gunicorn set-up
│   ├── Dockerfile.fast-ml
│   ├── gunicorn-config.py
│   └── start-server.sh
├── requirements.txt                -   Specify your python library dependencies in this file   
├── rest_api                        -   directory for creating REST API on top of ML application
│   ├── __init__.py
│   └── classifier_api.py           -   File to create REST API - POST request routes for ML model
├── testing                         
│   └── async_predictions.py        -   Useful for performance testing of Prediction API
└── wsgi.py                         -   File to start ML app as REST API


## Steps to run the example ML application as-is 
Example Machine learning application is a classifier model. Model training and testing modules are exposed as APIs , and sample datasets can be found in `./ML/data` directory
1. Clone the repository `git clone `.
2. Build docker container `docker build -t fast-api-ml .`
3. Run docker container  `docker run -d -p 8000:8000 fast-api-ml`
4. Open `http://127.0.0.1:8000/docs` which shows swagger UI
    *** swagger UI picture ***
5. Using swagger UI you can train and test ML model
    *** Training API picture ***
6. Performance testing of application on 1 Million post requests
    * ```python testing/async_predictions.py 1000```

## Customisation for your needs 




