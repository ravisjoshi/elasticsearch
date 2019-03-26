from datetime import datetime
from elasticsearch import Elasticsearch

es = Elasticsearch(['localhost:9200'])
doc = {
    'author': 'RaviJoshi',
    'text': 'Elasticsearch is a cool tool.',
    'timestamp': datetime.now(),
}
res = es.index(index="ravi", doc_type='tweet', id=1, body=doc)
print(res['result'])
res = es.get(index="ravi", doc_type='tweet', id=1)
print(res['_source'])
es.indices.refresh(index="ravi")
res = es.search(index="ravi", body={"query": {"match_all": {}}})
print("Got %d Hits:" % res['hits']['total'])
for hit in res['hits']['hits']:
    print("%(timestamp)s %(author)s: %(text)s" % hit["_source"])
