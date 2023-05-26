from pydantic import BaseModel, Field
from typing import Optional

class AylienSearchModel(BaseModel):
    #title: Optional[str]
    text: str #= Field(gt = 3, lt = 30)
    published_at_start: str = "NOW-1HOUR"
    published_at_end: str = "NOW"
    language: list = ["en", "ar"]
    #per_page: int = 50
    #aql : Optional[str]
    # categories_taxonomy: Optional[str]	
    # categories_id: Optional[list]
    # categories_confident: Optional[bool]
    # source_locations_country : Optional[str]
    # source_scopes_city: Optional[str]
    # entities_title_text : Optional[str]
    # entities_title_type : Optional[str]
    # entities_body_text : Optional[str]
    # entities_body_type : Optional[str]
    # entities_title_links_dbpedia: Optional[str]
    # entities_body_links_dbpedia: Optional[str]
    # sentiment_title_polarity: Optional[str]
    # sentiment_body_polarity: Optional[str]
    # source_domain : Optional[str]
    # not_source_domain: Optional[str]
    # source_locations_country: Optional[str]
    # not_source_locations_country:Optional[str]
    # source_locations_state: Optional[str]
    # not_source_locations_state:Optional[str]
    # source_locations_city:Optional[str]
    # not_source_locations_city: Optional[str]
    # source_scopes_country: Optional[str]
    # not_source_scopes_country: Optional[str]
    # source_scopes_state: Optional[str]
    # not_source_scopes_state:Optional[str]
    # source_scopes_city: Optional[str]
    # not_source_scopes_city: Optional[str]
    # source_scopes_level:Optional[str]
    # not_source_scopes_level: Optional[str]
    sort_by : str = 'published_at'


# class Expression(BaseModel):
#     expression: str = Field(gt = 3, lt = 30 )

class Region(BaseModel):
    region_name : str


class AylienSearchwithTopic(BaseModel):

    text: str #= Field(gt = 3, lt = 30)
    published_at_start: str = "NOW-1HOUR"
    published_at_end: str = "NOW"
    language: list = ["en", "ar"]
    categories_taxonomy: Optional[str]	
    categories_id: Optional[list]