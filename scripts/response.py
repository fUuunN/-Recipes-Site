from elasticsearch import Elasticsearch

def recipe_response(user_input: str):

    es = Elasticsearch(hosts='http://elastic:DkIedPPSCb@localhost:9200/')

    response = es.search(
        index='tarifler',
        body={
            "query": {
                "match": {
                    "Tarif Başlığı": user_input
                }
            },
            "size": 20
        }
    )

    if response['hits']['hits']:
        resultsAd = []
        resultsIcindekiler = []
        resultsAciklama = []
        resultsScore = []

        for hit in response['hits']['hits']:
            tarifAdi = hit['_source']['Tarif Başlığı']
            tarifIcindekiler = hit['_source']['Tarif İçindekiler']
            tarifAciklama = hit['_source']['Tarif Açıklama']
            score = hit['_score']
            
            resultsAd.append(tarifAdi)
            resultsIcindekiler.append(tarifIcindekiler)
            resultsAciklama.append(tarifAciklama)
            resultsScore.append(score)

        return resultsAd, resultsAciklama, resultsIcindekiler, resultsScore

    else:
        return "İlgili tarif bulunamadı."

