from art import text2art
from embed import Embedder
from es import ElasticSearcher
from elasticsearch import Elasticsearch
from pprint import pprint
import pandas as pd
# open topic xml
# for each topic
# - run query with es
# - store result
print(text2art('COVID-19 Browser'))
embedder = Embedder()
es_searcher = ElasticSearcher(index_name='lucene-index-cord19-2020-05-26-bm25')

query = 'corona'
topicid = '10'
query_emb = embedder([query])[0].tolist()
res = es_searcher(query_emb, topic=topicid)
df = pd.DataFrame.from_records(res.json)
df['topicid'] = topicid
print(df)