# txt with topicid Q0 docid rank score run-tag
import pandas as pd
from tqdm.autonotebook import tqdm
import pypeln.process as pr
from pathlib import Path

txt_path = './run-covid-2020-04-10-bm25.txt'
metadata_path = Path('./metadata.csv')

txt_df = pd.read_csv(txt_path, sep=' ', names=['topicid', 'Q0', 'docid', 'rank', 'score', 'run_tag'], header=None)
metadata = pd.read_csv(metadata_path)

print('Input text example:')
print(txt_df.head(5))
print('Metadata text example:')
print(metadata.head(5))
topicids, docids = txt_df['topicid'], txt_df['docid']
metadata['topicids'] = ''

# def convert(data):
#     topicid, docid = data
#     metadata.loc[metadata.cord_uid == docid, 'topicids'] += f' {topicid}'
#
# stage = tqdm(pr.map(convert, zip(topicids, docids), workers=4))
# list(stage)

for topicid, docid in tqdm(zip(topicids, docids)):
    metadata.loc[metadata.cord_uid == docid, 'topicids'] += f' {topicid}'

metadata = metadata[metadata.topicids != '']
out_path = metadata_path.parent / metadata_path.stem
out_path = str(out_path) + '-q.csv'
print(f'Final shape={metadata.shape}')
print('Output text example:')
print(metadata.head(5)['topicids'])
metadata.to_csv(out_path)
