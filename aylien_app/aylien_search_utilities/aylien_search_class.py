# BASIC IMPORTS
from aylien_app.schemas import request_models
import aylien_news_api
from aylien_news_api.rest import ApiException
from dotenv import load_dotenv
from aylien_app.schemas import aylien_response_models
import os
import json

class AylienSearch: 
    def __init__(self):
        self.aylien_instance = None
        
        with open("aylien_search_utilities/search_config.json", "r") as config_file:
            self.config_json = json.loads(config_file.read())

        self.AylienConnect()        
    
    
    def AylienConnect(self):
        load_dotenv()
        configuration = aylien_news_api.Configuration()
        configuration.api_key['X-AYLIEN-NewsAPI-Application-ID'] = os.getenv('APP_ID')
        configuration.api_key['X-AYLIEN-NewsAPI-Application-Key'] = os.getenv('APP_KEY')
        client = aylien_news_api.ApiClient(configuration)
        self.aylien_instance= aylien_news_api.DefaultApi(client)       


    def get_aylien_stories(self, search_input_model):
        try:
            stories_response = self.aylien_instance.list_stories(**search_input_model)
            return stories_response
        except ApiException as e:
            print("Exception when calling DefaultApi->list_stories: %s\n" % e)
            return e

    def default_stories(self):
        try:
            stories_response = self.aylien_instance.list_stories(
                text = "lebanon", 
                published_at_start="NOW-1HOUR", published_at_end="NOW"
            )
            return stories_response
        except ApiException as e:
            print("Exception when calling DefaultApi->list_stories: %s\n" % e)
            return e