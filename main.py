import pandas as pd
from art import text2art
from embed import Embedder
from es import ElasticSearcher
from elasticsearch import Elasticsearch
from pprint import pprint
from pyserini.search import pysearch
from tqdm.autonotebook import tqdm

# open topic xml
# for each topic
# - run query with es
# - store result
print(text2art('COVID-19 Browser'))
collection_name = 'covid_round3_udel'
embedder = Embedder()
es_searcher = ElasticSearcher(index_name='lucene-index-cord19-2020-05-19-bm25',
                              size=1000)
topics = pysearch.get_topics(collection_name)

bar = tqdm(topics)

dfs = []

for topicid in bar:
    query = topics[topicid]['query']
    bar.set_description(f"[{topicid}]{query[:40]}...")
    query_emb = embedder([query])[0].tolist()
    res = es_searcher(query_emb, topic=topicid)
    df = pd.DataFrame.from_records(res.json)
    df['topicid'] = topicid
    dfs.append(df)

final_df = pd.concat(dfs)
print(f"Final DataFrame shape={final_df.shape}")
print(final_df.head(5))
