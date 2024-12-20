import requests

class APIClient:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://financialmodelingprep.com/api/v3"

    def fetch_data(self, endpoint, symbol):
        url = f"{self.base_url}/{endpoint}/{symbol}?apikey={self.api_key}"
        response = requests.get(url)
        response.raise_for_status()
        return response.json()

    def get_financial_data(self, endpoint, symbol, key):
        data = self.fetch_data(endpoint, symbol)
        # Debugging: Log the data being fetched
        print(f"Fetched data for {symbol} ({endpoint}): {data}")
        # Handle missing keys gracefully
        try:
            return [item[key] for item in data[:5]]
        except KeyError:
            print(f"Key '{key}' missing in data for {symbol} ({endpoint})")
            return None

    def get_share_price(self, symbol):
        """
        Fetches the latest share price for the given symbol.
        """
        url = f"{self.base_url}/quote/{symbol}?apikey={self.api_key}"
        response = requests.get(url)
        response.raise_for_status()
        quote_data = response.json()
        if quote_data and len(quote_data) > 0:
            print(f"Share price for {symbol}: {quote_data[0]['price']}")  # Debugging
            return [quote_data[0]['price']]  # Returning as a list for consistency with other methods
        else:
            raise ValueError(f"Share price not found for {symbol}")
