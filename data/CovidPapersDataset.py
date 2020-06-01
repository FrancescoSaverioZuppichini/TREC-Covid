from torch.utils.data import Dataset
import pandas as pd

class CovidPapersDataset(Dataset):

    def __init__(self, df, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.df = df
        self.df = self.df[['title', 'authors', 'abstract', 'url', 'pubmed_id', 'topicids', 'cord_uid']]
        self.df.loc[:,'title'].fillna('', inplace = True)
        self.df.loc[:,'topicids'] = self.df.loc[:,'topicids'].apply(lambda x: x.split(' '))
        self.df = self.df[self.df['abstract'].notna()]
        self.df = self.df[self.df.abstract != '']
        self.df = self.df.reset_index(drop=True)
        self.df = self.df.fillna(0)
        
    def __getitem__(self, idx):
        row = self.df.loc[idx]
        self.df.loc[idx:, 'title_abstract'] = f"{row['title']} {row['abstract']}"
        return  self.df.loc[idx].to_dict()

    def __len__(self):
        return self.df.shape[0]
    
    @classmethod
    def from_path(cls, path, *args, **kwargs):
        df = pd.read_csv(path)
        return cls(df=df, *args, **kwargs)