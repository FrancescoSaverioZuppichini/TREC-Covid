from dataclasses import dataclass
from .Electra import ELECTRA
from sentence_transformers import models, SentenceTransformer

@dataclass
class Embedder:
    """
    This class uses Hugging's face transformers library to encode a list of strings into a 768 dim vetor.
    """
    model_name: str = 'gsarti/electra-msmarco-med-cord19-discriminator'
    max_seq_length: int  = 128
    do_lower_case: bool  = True
    model_type: str = 'electra'

    def __post_init__(self):
        self.word_embedding_model = self.get_model()
        # apply pooling to get one fixed vector
        self.pooling_model = self.get_pooling()

        self.model = SentenceTransformer(modules=[self.word_embedding_model, self.pooling_model])
    
    def get_model(self):
        if self.model_type == 'electra':
            return ELECTRA(
                self.model_name,
                max_seq_length=self.max_seq_length,
                do_lower_case=self.do_lower_case
            )
        elif self.model_type == 'bert':
            return models.BERT(
                self.model_name,
                max_seq_length=self.max_seq_length,
                do_lower_case=self.do_lower_case
            )
        else:
            raise AttributeError("Not supported")

    def get_pooling(self):
        return models.Pooling(self.word_embedding_model.get_word_embedding_dimension(),
                pooling_mode_mean_tokens=True,
                pooling_mode_cls_token=False,
                pooling_mode_max_tokens=False
            )

    def __call__(self, text: list):
        return self.model.encode(text) 