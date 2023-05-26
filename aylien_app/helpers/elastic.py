from elasticsearch import Elasticsearch
class ElasticIndex():

    def __init__(self, ip, port, cluster_name, index_name):
        self.ip = ip
        self.port = port
        self.elastic_client = None
        self.cluster_name = cluster_name
        self.index_name = index_name
        
        try: 
            self.connect()
        except Exception as e:
            print("Elastic connection failed! /n{}".format(e))

    def connect(self):
        es = Elasticsearch(["{}:{}".format(self.ip, self.port)])
        self.elastic_client = es

        return es


    def create_index(self, index_name):


        conf = {"settings": {"number_of_shards":1,
                "number_of_replicas": 1, 
                "index.mapping.total_fields.limit": 2000},

                "mappings": {"properties": {"@timestamp": { "type": "date", "format": "YYYY-MM-DD'T'HH:mm:ssZ"},
                                            "country" : {"type": "text"}, 
                                            "state" : {"type": "text"},
                                            "related_countries": {"type": "text"},
                                            "topic" : {"type": "text"},
                                            "title": {"type": "text"},
                                            "body": {"type": "text"},
                                            "categories" : {"type": "text"},
                                            "keywords": {"type": "text"},
                                            "source_website": {"type": "text"},
                                            "story_url": {"type": "text"},
                                            "location": {"type": "text"},
                                            "level": {"type": "text"},
                                            "urgency": {"type": "text"},
                                            "entities": {"type": "text"},
                                            "coverage_scope": {"type": "text"},
                                            "characters_count": {"type": "text"},
                                            "words_count": {"type": "text"},
                                            "title_sentiment": {"type": "text"},
                                            "text_sentiment": {"type": "text"}, 
                                            "media":  {"type": "text"} } }}
        try:
            self.elastic_client .indices.create(index = index_name, body=conf , ignore = 400)
            if self.elastic_client.indices.exists(index = index_name):
                raise DuplicateIndex 
        
        except Exception as e:
            print("Index creation failed", e)

    
    def delete_index(self, index_name):
        self.elastic_client.delete(index= index_name, ignore=[400])

    def insert_document(self, index_name,  document, refresh=False):
        try:
            return self.elastic_client.index(index=index_name,  body=document, refresh='wait_for', request_timeout=30)
        except Exception as e:
            print(e)

    def get_data(self, index_name, search_query, size=100):
        try:
            result = self.elastic_client.search(index=index_name, body=search_query, allow_partial_search_results=True,
                                           size=size, request_timeout=120)
            return result
        except Exception as e:
            print(e)

class DuplicateIndex(Exception): 
    def __init__(self):
        self.messsage = f"This index name exists. Please delete the duplicate or use a different index name"
