import requests

# URL de l'API TheMealDB pour obtenir une recette aléatoire
url = "https://www.themealdb.com/api/json/v1/1/random.php"

# Effectuer la requête GET à l'API
response = requests.get(url)

# Vérifier si la requête a réussi (code de statut 200)
if response.status_code == 200:
    # Extraire les données JSON de la réponse
    data = response.json()
    
    # Récupérer la première recette de la liste
    recipe = data["meals"][0]
    
    # Afficher les détails de la recette
    print("Nom de la recette :", recipe["strMeal"])
    print("Catégorie :", recipe["strCategory"])
    print("Instructions :", recipe["strInstructions"])
    print("Liste des ingrédients :")
    for i in range(1, 21):
        ingredient = recipe[f"strIngredient{i}"]
        measure = recipe[f"strMeasure{i}"]
        if ingredient and measure:
            print(f"- {measure} {ingredient}")
else:
    print("Une erreur s'est produite lors de la requête à l'API.")