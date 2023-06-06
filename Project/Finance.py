import yfinance as yf
import matplotlib.pyplot as plt
import datetime

# Récupération des données du cours de l'action Apple sur la dernière semaine
symbol = "AAPL"
end_date = datetime.datetime.now()
start_date = end_date - datetime.timedelta(days=365)

data = yf.download(symbol, start=start_date, end=end_date)

if not data.empty:
    # Extraction des prix de clôture
    timestamps = data.index
    prices = data["Close"]

    # Création du graphique
    plt.plot(timestamps, prices)
    plt.xlabel("Date")
    plt.ylabel("Prix de clôture")
    plt.title(f"Cours de l'action {symbol} - Dernière semaine")
    plt.xticks(rotation=45)
    plt.show()
else:
    print("Erreur lors de la récupération des données du cours de l'action.")
