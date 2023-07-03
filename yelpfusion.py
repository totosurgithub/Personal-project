import requests

# URL de l'API Yelp Fusion pour rechercher des restaurants
url = "https://api.yelp.com/v3/businesses/search"

# Paramètres de la requête (vous pouvez ajuster ces paramètres selon vos besoins)
params = {
    "term": "restaurant",
    "location": "Paris",  # Exemple : recherche de restaurants à Paris
    "limit": 10  # Limite le nombre de résultats à 10
}

# Client ID et API key Yelp Fusion
client_id = "yewZhSiALaCJljVb840eoA"
api_key = "oqB87dnp1tQTEe2agQP50HTc79QyGngj7zxObb-8ZDcwfai24soZfOPEVuZfx_huFYjbo0Wcwz3GduLYuLQ6Mi8zYN4uhS5cgf_kgGkAN4mL6NJZcIJegwOynjmjZHYx"

# Entête d'autorisation contenant le client ID et l'API key
headers = {
    "Authorization": f"Bearer {api_key}",
    "User-Agent": "My-App",
    "X-Yelp-Client-ID": client_id
}

# Effectuer la requête GET à l'API Yelp Fusion
response = requests.get(url, params=params, headers=headers)

# Vérifier si la requête a réussi (code de statut 200)
if response.status_code == 200:
    # Extraire les données JSON de la réponse
    data = response.json()
    
    # Parcourir les restaurants et afficher leurs informations
    for business in data["businesses"]:
        print("Nom :", business["name"])
        print("Note :", business["rating"])
        print("Adresse :", ", ".join(business["location"]["display_address"]))
        print("Téléphone :", business["phone"])
        
        # Vérifier si des statistiques sont disponibles
        if "review_count" in business:
            print("Nombre d'avis :", business["review_count"])
        if "rating" in business:
            print("Note moyenne :", business["rating"])
        if "price" in business:
            print("Prix :", business["price"])
        if "categories" in business:
            categories = [category["title"] for category in business["categories"]]
            print("Catégories :", ", ".join(categories))
        print("----------")
else:
    # Afficher la réponse d'erreur
    print("Erreur", response.status_code)
    print("Message d'erreur :", response.text)
