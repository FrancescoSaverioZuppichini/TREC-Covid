# lucene
python index2txt.py --index ../dataset/index/lucene-index-cord19-abstract-2020-05-19 --hits 1500 --tag lucene-index-cord19-abstract-2020-05-19 --out ../dataset/submission-bm25
python index2txt.py --index ../dataset/index/lucene-index-cord19-full-text-2020-05-19 --hits 1500 --tag lucene-index-cord19-full-text-2020-05-19 --out ../dataset/submission-bm25
python index2txt.py --index ../dataset/index/lucene-index-cord19-paragraph-2020-05-19 --hits 1500 --tag lucene-index-cord19-paragraph-2020-05-19 --out ../dataset/submission-bm25
# tommaso
python index2txt.py --index ../dataset/index/tommaso-index-cord19-abstract-2020-05-19 --hits 1500 --tag tommaso-index-cord19-abstract-2020-05-19 --out ../dataset/submission-bm25
python index2txt.py --index ../dataset/index/tommaso-index-cord19-full-text-2020-05-19 --hits 1500 --tag tommaso-index-cord19-full-text-2020-05-19 --out ../dataset/submission-bm25
python index2txt.py --index ../dataset/index/tommaso-index-cord19-paragraph-2020-05-19 --hits 1500 --tag tommaso-index-cord19-paragraph-2020-05-19 --out ../dataset/submission-bm25
