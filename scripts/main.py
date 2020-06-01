"""
Creazione di una pipeline in Pyserini per fare l'equivalente di quello che facevano loro per la submission al round 2
(BM25 sui topic del round 2 di TREC-EVAL usando la versione UDel) usando l'index full text che dia in output i top 500 hits.
"""

"""
# TODO
- index for lucine
- get queries from challange
- SimpleSearcher
# ISSUES
- not all paper have
- be sure the ids are the cord_id
# Get the data
!wget https://www.dropbox.com/s/j55t617yhvmegy8/lucene-index-covid-2020-04-10.tar.gz

!tar xvfz lucene-index-covid-2020-04-10.tar.gz

"""
import requests
import xmltodict
import json
import pprint
import pandas as pd
from pathlib import Path
from pyserini.search import pysearch
from tqdm.autonotebook import tqdm
from dataclasses import dataclass
# from https://github.com/gsarti/covid-papers-browser/blob/feature/TREC/trec/exploration.ipynb
TOPIC_SET_URL = 'https://ir.nist.gov/covidSubmit/data/topics-rnd2.xml'
INDEX_PATH = 'lucene-index-covid-2020-04-10'
NUMBER_OF_HITS = 500
RUN_TAG = 'test'

topic_set_xml = requests.get(TOPIC_SET_URL).text

@dataclass
class PreFetchingDocumentsWithLucene:
    queries: [str]
    searcher: pysearch.SimpleSearcher
    number_of_hits: int = 1000

    def __call__(self):
        self.query_hits = {}
        print('Running {} queries in total'.format(len(self.queries)))
        for id, query in enumerate(tqdm(self.queries)):
            # id in our case is just the number of the topics in order
            self.query_hits[query] = self.searcher.search(query, self.number_of_hits)
        print(f'Queries completed')

    def to_txt(self, out_path):
        with open(out_path, 'w') as runfile:
            for id, hits in enumerate(self.query_hits.values()):
                for i in range(0, len(hits)):
                    # submission format topicid Q0 docid rank score run-tag
                    _ = runfile.write('{} Q0 {} {} {:.6f} {}\n'.format(id, hits[i].docid, i+1, hits[i].score, RUN_TAG))

    def to_metadata(self, metadata_path: Path):
        metadata = pd.read_csv(metadata_path)
        metadata['quids'] = ''
        for quid, hits in enumerate(tqdm(self.query_hits.values())):
            for i in range(len(hits)):
                docid = hits[i].docid
                # serialize array with queries ids as string of numbers
                if (metadata.cord_uid == docid).any():
                    val = metadata.loc[metadata.cord_uid == docid, 'quids'].values[0]
                    metadata.loc[metadata.cord_uid == docid, 'quids'] += f',{quid}' if val != '' else str(quid)

        metadata = metadata[metadata.quids != '']
        out_path = metadata_path.parent / metadata_path.stem
        out_path = str(out_path) + '-q.csv'
        print(f'Final shape={metadata.shape}')
        print(metadata.head(5)['quids'])
        metadata.to_csv(out_path)

        return out_path

    @classmethod
    def from_round_xml(cls, xml, *args, **kwargs):
        topic_set = xmltodict.parse(topic_set_xml)
        topics = topic_set['topics']['topic'] # [...,('query', 'coronavirus recovery'),...]
        queries = [x['query'] for x in topics]
        return cls(queries, *args, **kwargs)


searcher = pysearch.SimpleSearcher(INDEX_PATH)
pip = PreFetchingDocumentsWithLucene.from_round_xml(topic_set_xml, searcher, number_of_hits=1000)
pip.searcher.set_bm25_similarity(0.9, 0.4) # we should open an issue
pip()
# pip.to_metadata(Path('./metadata.csv'))
pip.to_txt('run-covid-2020-04-10-bm25.txt')
#
