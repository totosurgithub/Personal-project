import boto3
from textblob import TextBlob

# Connexion à l'API Amazon
product_advertising = boto3.client('product-advertising',
                                  aws_access_key_id='YOUR_ACCESS_KEY',
                                  aws_secret_access_key='YOUR_SECRET_KEY',
                                  region_name='REGION_NAME') #à compléter avec les identifiants

# Récupération des commentaires de produits
def get_product_reviews(product_id):
    response = product_advertising.get_product_reviews(
        ItemId=product_id,
        LanguageCode='fr_FR',
        MarketplaceId='A13V1IB3VIYZZH'
    )
    return response['Reviews']

# Analyse de sentiment pour un commentaire
def sentiment_analysis(review_text):
    analysis = TextBlob(review_text)
    if analysis.sentiment.polarity > 0:
        return 'positive'
    elif analysis.sentiment.polarity == 0:
        return 'neutral'
    else:
        return 'negative'

# Programme principal
if __name__ == '__main__':
    product_id = 'B08T1HR5CS' #fill with product id
    reviews = get_product_reviews(product_id)
    for review in reviews:
        sentiment = sentiment_analysis(review['Content'])
        print(review['Content'], '-', sentiment)


# La fonction get_product_reviews récupère les commentaires de produits pour un produit donné en utilisant boto3. 
# Nous utilisons la fonction sentiment_analysis pour effectuer une analyse de sentiment simple en utilisant TextBlob.
#Vous devez remplacer YOUR_PRODUCT_ID avec l'ID du produit pour lequel vous souhaitez récupérer les commentaires. 
# De plus, veuillez noter que cet exemple ne prend en compte que les commentaires en français, 
#vous pouvez donc changer la valeur de LanguageCode pour prendre en compte d'autres langues.