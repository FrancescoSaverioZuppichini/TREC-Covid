# TREC

https://ir.nist.gov/covidSubmit/

Lucene indexes from https://github.com/castorini/anserini/blob/master/docs/experiments-cord19.md

Fused link https://github.com/castorini/anserini/blob/master/docs/experiments-covid.md

```
python src/main/python/fusion.py --method RRF --max_docs 10000 --out runs/anserini.covid-r3.fusion1.txt \
 --runs runs/anserini.covid-r3.abstract.qq.bm25.txt runs/anserini.covid-r3.full-text.qq.bm25.txt runs/anserini.covid-r3.paragraph.qq.bm25.txt
```