from elasticsearch import Elasticsearch
from elasticsearch.helpers import scan

# creating a elastic search instance
es = Elasticsearch([{'host': 'localhost', 'port': 9200,
                     'scheme': "http"}], verify_certs=True)
# es = Elasticsearch(['http://localhost:9200/'], verify_certs=True) #Method 2

# check the connectivity of the elastic search
print(es.ping())

# Deleting
#DELETE /testing/22
# deleting the data from the index testing --->DELETE /testing/22
es.delete(index="testing", id=22)

# Dropping the index
#DELETE /testing123
es.indices.delete(index='testing123', ignore=[400, 404])

# Inserting the data in indeces
# POST testing/_doc/23
# {
#     "name":"Programming Fundamentals",
#     "mobile":"94575154512",
#     "address":"56"
# }
es.index(index='testing', id=23, document={
    "name": "Programming Fundamentals",
    "mobile": "94575154512",
    "address": "56"
})

# List all the indices in the ElasticSearch
#GET /_cat/indices
print(es.indices.get_alias().keys())

# Get all the data from a particular indices
# GET testing/_search
rel = scan(client=es,
           index='testing',
           raise_on_error=True,
           preserve_order=False,
           clear_scroll=True)
result = list(rel)
print(result[2])  # select all data from an indices --->GET testing/_search
