# tommaso
python ./fusion.py --method RRF --max_docs 1500 --out ../dataset/submission-bm25-fused/tommaso-index-cord19-2020-05-19-bm25.txt \
 --runs ../dataset/submission-bm25/tommaso-index-cord19-abstract-2020-05-19-bm25.txt \
  ../dataset/submission-bm25/tommaso-index-cord19-full-text-2020-05-19-bm25.txt \
  ../dataset/submission-bm25/tommaso-index-cord19-paragraph-2020-05-19-bm25.txt
# lucene
python ./fusion.py --method RRF --max_docs 1500 --out ../dataset/submission-bm25-fused/lucene-index-cord19-2020-05-26-bm25.txt \
 --runs ../dataset/submission-bm25/lucene-index-cord19-abstract-2020-05-26-bm25.txt \
  ../dataset/submission-bm25/lucene-index-cord19-full-text-2020-05-26-bm25.txt \
  ../dataset/submission-bm25/lucene-index-cord19-paragraph-2020-05-26-bm25.txt