from elasticsearch5 import Elasticsearch  

ES = [
    '10.200.64.50:9200'
]


es = Elasticsearch(
    ES,
    sniff_on_start=True,
    sniff_on_connection_fail=True,
    sniffer_timeout=60
)

query = {"query":{"match_all":{}}}
ret = es.search(index='ld.case.rule.20190630.other', doc_type='esbasejudgement', body=query)

print(ret)
