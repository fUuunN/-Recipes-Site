from response import recipe_response

resultsAd = []
resultsIcindekiler = []
resultsAciklama = []
resultsScore = []


resultsAd,resultsAciklama,resultsIcindekiler,resultsScore = recipe_response("Kabak")

for deger in range(len(resultsAd)):
    print(resultsAd[deger])
    print("\n")
    print(resultsIcindekiler[deger])
    print(len(resultsIcindekiler[deger]))
    print("\n")
    print(resultsAciklama[deger])
    print(len(resultsAciklama[deger]))
    print("\n")
    print(resultsScore[deger])

print(len(resultsAd))
print(len(resultsAciklama))
print(len(resultsIcindekiler))
print(len(resultsScore))

    