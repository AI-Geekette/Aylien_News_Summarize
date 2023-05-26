from ast import Bytes
from cgitb import text
from fastapi import FastAPI
import json
import time, datetime
from routes import countries_routes, custom_routes
from schemas.request_models import AylienSearchModel, AylienSearchwithTopic
import schedule
import requests


agent_app = FastAPI(title = " News collector agent - scheduled")

agent_app.include_router(countries_routes.countries_router)
agent_app.include_router(custom_routes.custom_search_router)

regions = {"region1": ["lebanon", "syria", "israel"], "region2": ["turkey", "iran", "iraq"], "region3": ["palestine", "israel"]}
hot_topics = ["ukraine russia conflict", "russia sanctions", "war on ukraine", "russia putin"]


@schedule.repeat(schedule.every(1).minutes)
def _by_country_news(country):
    
    api_endpoint = "http://127.0.0.1:8000/news/countries/"
  
    request_body = AylienSearchModel()
    request_body.text = country

    response = requests.post(url=api_endpoint, data=request_body)
    print(response)

# while True:
#     schedule.run_pending()
#     time.sleep(3)

def news_by_country(country):
    
  api_endpoint = "http://127.0.0.1:8000/news/countries/"

  request_body = AylienSearchModel(text = country)

  response = requests.post(url=api_endpoint, data=request_body)
  print(response)

  


