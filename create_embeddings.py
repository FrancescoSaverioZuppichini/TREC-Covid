import json
import argparse
import pprint 
from torch.utils.data import DataLoader
from embed import CovidPapersEmbeddedAdapter, Embedder
from es import ElasticSearchProvider
from data import CovidPapersDataset
from Project import Project
from tqdm.autonotebook import tqdm
from pathlib import Path

parser = argparse.ArgumentParser(
        description='Create the embeddings')

parser.add_argument('--metadata',
                    type=str, required=True,
                    help='Path to the metadata file')
args = parser.parse_args()

metadata_path = Path(args.metadata)

pr = Project()
# lucene-index-cord19-2020-05-26-bm25
# tommaso-index-cord19-2020-05-26-bm25
# prepare the data
name = metadata_path.stem
print(f'Creating embedding from {name}')

ds = CovidPapersDataset.from_path(metadata_path)
dl = DataLoader(ds, batch_size=128, num_workers=4, collate_fn=lambda x: x)

with open(pr.base_dir / 'es_index.json', 'r') as f:
    index_file = json.load(f)
    es_provider = ElasticSearchProvider(index_file, index_name=name)
    # see all at http://localhost:9200/lucene-index-cord19-2020-05-26-bm25/_search?pretty=true&q=*:*
# create the adpater for the data
es_adapter = CovidPapersEmbeddedAdapter()
# drop the dataset
es_provider.drop()
# create a new one
es_provider.create_index()

embedder = Embedder(model_type='electra')

for batch in tqdm(dl):
    x = [b['title_abstract'] for b in batch]
    embs = embedder(x)
    es_provider(es_adapter(batch, embs))