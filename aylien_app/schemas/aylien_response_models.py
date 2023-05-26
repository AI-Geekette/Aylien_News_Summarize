from pydantic import BaseModel

class story_model(BaseModel):
    country: str ="NA"
    state: str = "NA"
    related_countries: str = "NA"
    topic : str = "NA"
    characters_count : int = 0
    words_count : int = 0
    title : str ="NA"
    title_sentiment : str ="NA"
    text_sentiment : str ="NA"
    text : str ="NA"
    categories : str ="NA"
    keywords : str ="NA"
    website : str ="NA"
    url : str ="NA"
    source_location : str ="NA"
    coverage_scope : str ="NA"
    geographical_level : str ="NA"
    media: str ="NA"
    urgency_score : str  = "NA"
    entities : str = "NA"
    origin_datasource : str = "Aylien API"

class unified_response_model(BaseModel):
    country: str ="NA"
    state: str = "NA"
    related_countries: str = "NA"
    topic : str = "NA"
    base: story_model


