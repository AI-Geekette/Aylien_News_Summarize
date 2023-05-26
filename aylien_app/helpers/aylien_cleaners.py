from aylien_app.schemas import aylien_response_models
import re

class cleaners: 
    def __init__(self):
        pass
    
    def text_cleaner(self, text): 

        """ role """

        bad_chars = '[",“”]'
        clean_text = re.sub(bad_chars, "", text)
        clean_text = re.sub('"', '', clean_text)
        clean_text = re.sub("\n", '', clean_text)
        clean_text = re.sub("'", '', clean_text)
        return clean_text
    
    def basic_story_handler(self, story):

        """ converts the aylien response into the basic fields of our model response """

        parsed_story = aylien_response_models.story_model()
        obj = story.to_dict()
        parsed_story.title = obj["title"] 
        parsed_story.text = self.text_cleaner(obj['body'])
        story_categories = obj["categories"]
        story_labels_with_ids = [f"{story_cat['label']}_{story_cat['id']}" for story_cat in story_categories]
        parsed_story.categories = "|".join(story_labels_with_ids)
        parsed_story.keywords = "|".join(obj['keywords'])
        parsed_story.website = obj['source']['home_page_url']
        parsed_story.url = obj['links']['permalink']
        
        locations = obj['source']['locations']
        if len(locations)<1: 
                parsed_story.source_location = "NA"
        else:
            src_loc = [loc if loc != None else "NA" for loc in locations[0].values()]
            parsed_story.source_location = "|".join(src_loc)
        
        story_coverage_scopes = obj['source']['scopes']
        if len(obj['source']['scopes'])<1: 
            parsed_story.coverage_scope = "NA"
        else: 
            scope = [val if val != None else "NA" for val in story_coverage_scopes[0].values()]
            parsed_story.coverage_scope = "|".join(scope)
        
        parsed_story.characters_count = obj['characters_count']
        parsed_story.words_count = obj['words_count']
        parsed_story.title_sentiment = obj['sentiment']["title"]["polarity"] if obj['sentiment']["title"]["score"]> 0.4 else "maybe " + obj['sentiment']["title"]["polarity"]
        parsed_story.text_sentiment  = obj['sentiment']["body"]["polarity"] if obj['sentiment']["body"]["score"]> 0.4 else "maybe " + obj['sentiment']["body"]["polarity"]
        parsed_story.geographical_level ='NA' if len(story_coverage_scopes)<1 else story_coverage_scopes[0]["level"]
        parsed_story.entities = 'NA'
        
        return parsed_story
