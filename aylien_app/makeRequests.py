import string
import requests
import os
import getpass
from dotenv import load_dotenv
import json
import openai

# load_dotenv()
# OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
# openai_api_key = getpass.getpass('OpenAI API Key:')

api_url = 'http://127.0.0.1:8000/'

def make_custom_request(custom_keyword: string):
        
    # API endpoint URL
    ENDPOINT = api_url+'custom/'+custom_keyword
    # Make the API request
    payload = {
    "text": "string",
    "published_at_start": "NOW-1HOUR",
    "published_at_end": "NOW",
    "language": [
        "en",
        "ar"
    ],
    "sort_by": "published_at"
    }
    response = requests.post(ENDPOINT , json=payload)
    response_json = response.json()
    news_list = response_json[1] # This is a list of the news objects
    return {'results': news_list}

def data_to_summarize(api_response):
    
    # You can add a filter with more fields than text and modify the list comprehension
    # Filter specific fields from each object in the list
    filtered_data = [resp["text"] for resp in api_response]
    # all_news = ' '.join(filtered_data)
    return {"news_list": filtered_data}

def summarize(input_data:string):
    import openai 
    openai.api_key = os.getenv("OPENAI_API_KEY")
    summary_list =[]
    for news in input_data:
        prompt= news + "\n Tl;dr:"
        response = openai.Completion.create(
        model="text-curie-001",
        prompt=prompt,
        temperature=0.7,
        max_tokens=1000,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=1
        )
        summary_list.append({"original_news":news, "summarized_news":response["choices"][0]["text"]})
        return {"results": summary_list}
# FOR BASIC TESTING    
# def main():
    
#     keywords_default = 'bitcoin'
#     first_response = make_custom_request(keywords_default)
#     print("API RESPONSE: \n", first_response, '\n\n')
#     clean_data = data_to_summarize(first_response['results'])
#     print("API RESPONSE: \n", clean_data, '\n\n')
    
#     summaries = summarize(clean_data["news_list"][:3])
#     # print(summaries)
#     # file_path = './summaries.json'
#     # with open(file_path, "w") as file:
#     #     json.dump(summaries, file)
#     return {"API_RESPONSE": clean_data["news_list"][:3], "PREPROCESSED_DATA": summaries}

# res = main()
# print(res)