import requests
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

# -------------------------------
# 🔧 SETTINGS
# -------------------------------
COINS = ["bitcoin", "ethereum", "dogecoin"]
CURRENCY = "usd"
API_URL = f"https://api.coingecko.com/api/v3/simple/price"

# -------------------------------
# 🧩 FETCH DATA FROM COINGECKO API
# -------------------------------
def fetch_crypto_prices():
    try:
        response = requests.get(API_URL, params={
            "ids": ",".join(COINS),
            "vs_currencies": CURRENCY,
            "include_24hr_change": "true"
        })
        data = response.json()
        return data
    except Exception as e:
        print("Error fetching data:", e)
        return None

# -------------------------------
# 🧮 SAVE TO EXCEL
# -------------------------------
def save_to_excel(df):
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"crypto_prices_{timestamp}.xlsx"
    df.to_excel(filename, index=False)
    print(f"✅ Data saved to {filename}")

# -------------------------------
# 📊 VISUALIZE PRICE TRENDS
# -------------------------------
def visualize_prices(df):
    plt.figure(figsize=(8, 5))
    plt.bar(df["Coin"], df["Price (USD)"])
    plt.title("Current Cryptocurrency Prices")
    plt.xlabel("Cryptocurrency")
    plt.ylabel("Price (USD)")
    plt.grid(True, linestyle="--", alpha=0.5)
    plt.tight_layout()
    plt.show()

# -------------------------------
# 🚀 MAIN FUNCTION
# -------------------------------
def main():
    print("📡 Fetching latest crypto prices...")
    data = fetch_crypto_prices()

    if not data:
        print("Failed to retrieve data. Try again later.")
        return

    records = []
    for coin in COINS:
        coin_data = data.get(coin, {})
        records.append({
            "Coin": coin.capitalize(),
            "Price (USD)": coin_data.get(CURRENCY, 0),
            "24h Change (%)": round(coin_data.get(f"{CURRENCY}_24h_change", 0), 2),
            "Fetched At": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        })

    df = pd.DataFrame(records)
    print("\n📊 Current Crypto Prices:\n")
    print(df)

    save_to_excel(df)
    visualize_prices(df)

if __name__ == "__main__":
    main()
