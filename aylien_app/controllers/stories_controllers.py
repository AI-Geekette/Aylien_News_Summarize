import json
from aylien_app.schemas import aylien_response_models
from aylien_search_utilities import aylien_search_class
from schemas import request_models
from helpers import aylien_cleaners

class aylien_services:

    def __init__(self):
        self.search_module = aylien_search_class.AylienSearch()
    
    def test_get(self):
        
        """ This is a simple get method for testing that makes a query on aylien api 
        with a hardcoded search parameter about Lebanon for last hour"""

        response_obj = self.search_module.default_stories()
        if len(response_obj.stories)>0:
            jsonable_response = self.clean_news_response(response_obj, {"NA": "NA"})
            return jsonable_response
        else:
            return {"message": "Aylien API returned an empty list of stories"}


    def post_all_params(self, search_input: request_models.AylienSearchModel):
        
        """ This is a post method for general querying of news from aylien with
        a curl+dict search parameters"""

        response_obj = self.search_module.get_aylien_stories(search_input.dict())

        if len(response_obj.stories)>0:
            jsonable_response = self.clean_news_response(response_obj, {"NA": "NA"})
            return jsonable_response
        else:
            return {"message": "Aylien API returned an empty list of stories"}
    
    
    def post_all_params_with_country(self, country, search_input: request_models.AylienSearchModel):
    
        """ This is a post method that sets the country value in the query search model"""

        search_input.text = country
        response_obj = self.search_module.get_aylien_stories(search_input.dict())
        if len(response_obj.stories)>0:
            jsonable_response = self.clean_news_response(response_obj, {"country": country})
            return jsonable_response
        else:
            return {"message": "Aylien API returned an empty list of stories"}


    def post_params_with_topic(self, general_topic, search_input: request_models.AylienSearchwithTopic):
        
        """ This is a post that sets a topic parameters in the query search model"""
        
        config_file = self.search_module.config_json

        if general_topic not in config_file["topics_list"]:
            return {"message": "Topic not defined. Choose from this list \n{}".format(config_file["topics_list"])}
        
        elif general_topic in config_file["topics_list"]:
            search_input.categories_taxonomy = config_file["categories_per_topic"][general_topic]["categories_taxonomy"]
            search_input.categories_id = list(config_file["categories_per_topic"][general_topic]["catgories_pool"].keys())

        response_obj = self.search_module.get_aylien_stories(search_input.dict())
        if len(response_obj.stories)>0:
            jsonable_response = self.clean_news_response(response_obj, {"topic": "whatever"})
            return jsonable_response
        else:
            return {"message": "Aylien API returned an empty list of stories"}

    
    def post_custom_keywords(self, keywords, search_input: request_models.AylienSearchModel):
    
        """ This is a post method that sets a custom expression or keywords values in the query search model"""

        search_input.text = keywords

        response_obj = self.search_module.get_aylien_stories(search_input.dict())
        
        if len(response_obj.stories)>0:
            jsonable_response = self.clean_news_response(response_obj,{"NA": "NA"})
            return keywords, jsonable_response
        else:
            return {"message": "Aylien API returned an empty list of stories"}


    def clean_news_response(self, aylien_response, params:dict):
        """ This function restructures aylien response object into our response model
        inputs: 
        aylien_response: the object returned by aylien api
        
        return: 
        json_load: a json object of the parsed response model defined"""
        parsed_resp = [] 
        print(params)                                                           # initialize list to store cleaned article data

        for story in aylien_response.stories:
            parsed_story = aylien_cleaners.cleaners().basic_story_handler(story)
            for param in list(params.keys()):
                
                if param=="topic":
                    parsed_story.country = "NA"
                    parsed_story.topic = params["topic"]
                elif param=="country":
                    parsed_story.country = params["country"]
                elif param=="state": 
                    parsed_story.state = params["state"]
            parsed_resp.append(parsed_story.dict())

        json_resp = json.dumps(parsed_resp)
        json_load = json.loads(json_resp)

        return json_load