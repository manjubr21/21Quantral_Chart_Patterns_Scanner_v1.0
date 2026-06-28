from app.data.providers.yahoo_provider import YahooProvider

provider = YahooProvider()

candles = provider.get_history(
    symbol="RELIANCE",
    timeframe="1d",
    limit=5,
)

print(f"Downloaded {len(candles)} candles\n")

for candle in candles:
    print(candle)