import yfinance as yf
import matplotlib.pyplot as plt
import datetime
import ta

# Récupération des données du cours de l'action Apple sur la dernière semaine
symbol = "TSLA" #pour ajouter le cac40, préciser .PA
end_date = datetime.datetime.now()
start_date = end_date - datetime.timedelta(days=60)

data = yf.download(symbol, start=start_date, end=end_date)

if not data.empty:
    # Extraction des prix de clôture
    timestamps = data.index
    prices = data["Close"]

    # Calcul des indicateurs techniques
    sma = ta.trend.sma_indicator(prices, window=20)
    rsi = ta.momentum.rsi(prices, window=14)

    # Création du graphique
    plt.plot(timestamps, prices, label="Prix de clôture")
    plt.plot(timestamps, sma, label="SMA (20)")
    plt.xlabel("Date")
    plt.ylabel("Prix de clôture")
    plt.title(f"Cours de l'action {symbol} - Dernière semaine")
    plt.xticks(rotation=45)
    plt.legend()

    # Commentaire sur la tendance
    last_price = prices[-1]
    last_sma = sma[-1]
    last_rsi = rsi[-1]

    if last_price > last_sma and last_rsi > 50:
        comment = "Tendance haussière (bullish)"
    else:
        comment = "Tendance baissière (bearish)"

    plt.figtext(0.5, 0.02, comment, ha="center")

    plt.show()
else:
    print("Erreur lors de la récupération des données du cours de l'action.")
