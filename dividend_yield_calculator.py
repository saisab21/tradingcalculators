def dividend_yield_calculator(inputs):
    """
    Calculates the dividend yield of a stock based on its annual dividend and current price.

    Parameters:
    inputs (dict): A dictionary with the following keys:
        - 'annual_dividend' (float): Annual dividend per share.
        - 'stock_price' (float): Current price of the stock.

    Returns:
    dict: A dictionary with the dividend yield percentage.
    """
    try:
        # Extract values from inputs with validation
        annual_dividend = float(inputs.get('annual_dividend', 0))
        stock_price = float(inputs.get('stock_price', 0))

        if annual_dividend < 0 or stock_price <= 0:
            return {"error": "Annual dividend must be non-negative and stock price must be positive."}

        # Calculate dividend yield
        dividend_yield = (annual_dividend / stock_price) * 100  # Yield in percentage

        return {
            "annual_dividend": annual_dividend,
            "stock_price": stock_price,
            "dividend_yield": round(dividend_yield, 2)
        }

    except ValueError:
        return {"error": "Invalid input: Ensure all inputs are numbers."}
    except Exception as e:
        return {"error": f"An unexpected error occurred: {e}"}

# Example usage
inputs = {
    "annual_dividend": 5,
    "stock_price": 100
}

result = dividend_yield_calculator(inputs)
print(result)
