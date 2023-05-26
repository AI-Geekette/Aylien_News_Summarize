from __future__ import print_function
import time
import aylien_news_api
from aylien_news_api.rest import ApiException
from pprint import pprint
import json

configuration = aylien_news_api.Configuration()
configuration.api_key['X-AYLIEN-NewsAPI-Application-ID'] = 'b04d4f01'
configuration.api_key['X-AYLIEN-NewsAPI-Application-Key'] = '3032c7fa7a67bf041b858edaf42bbd0b'

client = aylien_news_api.ApiClient(configuration)
api_instance = aylien_news_api.DefaultApi(client)

try:
    api_response = api_instance.list_stories(
        language = ['en', 'ar'],
        text = "Lebanon",
        published_at_start='NOW-1DAY',
        published_at_end='NOW', 
        categories_taxonomy= 'iptc-subjectcode', 
        categories_id= ['16011000', '11021000', '11005000', '09009000', '06006009', '06006000', '04019001', '04016007', '04008036', '04008019', '04008010', '04008016', '04008015', '04008008', '04008001', '04008000']
    )
    #pprint(api_response)
    # with open("api_resuts.txt", "w") as file: 
    #     file.write(str(api_response))
    #pprint(api_response.stories[0])
    example_res = api_response
    with open("example_response.txt", "w") as file: 
        file.write(str(example_res))

    # news_story = api_response.stories[0].to_dict()
    # #pprint(type(news_story))
    # story_body = news_story['body']
    # story_categories = news_story['categories']
    # story_labels_with_ids = [(story_cat['label'], story_cat['id']) for story_cat in story_categories]
    # story_keywords = news_story['keywords']
    # story_source = news_story['source']['home_page_url']
    # story_url = news_story['links']['permalink']
    # story_location = news_story['source']['locations']
except ApiException as e:
    print("Exception when calling DefaultApi->list_stories: %s\n" % e)