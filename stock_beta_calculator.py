import yfinance as yf
import numpy as np

def stock_beta_calculator(inputs):
    """
    Calculates the beta of a stock compared to the market index.

    Parameters:
    inputs (dict): A dictionary with the following keys:
        - 'stock_ticker' (str): Ticker symbol of the stock.
        - 'market_ticker' (str): Ticker symbol of the market index (e.g., '^GSPC' for S&P 500).
        - 'period' (str): Period for historical data (e.g., '1y' for one year).

    Returns:
    dict: A dictionary with the calculated beta value or an error message.
    """
    try:
        stock_ticker = inputs.get('stock_ticker')
        market_ticker = inputs.get('market_ticker')
        period = inputs.get('period', '1y')

        # Fetch historical data
        stock_data = yf.download(stock_ticker, period=period)['Close'].pct_change().dropna()
        market_data = yf.download(market_ticker, period=period)['Close'].pct_change().dropna()

        if stock_data.empty or market_data.empty:
            return {"error": "Could not fetch sufficient data for calculation."}

        # Calculate covariance and variance
        covariance = np.cov(stock_data, market_data)[0][1]
        market_variance = np.var(market_data)

        beta = covariance / market_variance

        return {
            "stock_ticker": stock_ticker,
            "market_ticker": market_ticker,
            "beta": round(beta, 2)
        }

    except Exception as e:
        return {"error": f"An unexpected error occurred: {e}"}

# Example usage
inputs = {
    "stock_ticker": "AAPL",
    "market_ticker": "^GSPC",  # S&P 500
    "period": "1y"
}

result = stock_beta_calculator(inputs)
print(result)
