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
    # Extract values from inputs
    annual_dividend = inputs.get('annual_dividend', 0)
    stock_price = inputs.get('stock_price', 0)
    
    # Calculate dividend yield
    dividend_yield = (annual_dividend / stock_price * 100) if stock_price > 0 else 0

    # Output dictionary
    output = {
        "annual_dividend": annual_dividend,
        "stock_price": stock_price,
        "dividend_yield": round(dividend_yield, 2)  # Yield in percentage
    }
    
    return output

# Example usage
inputs = {
    "annual_dividend": 5,
    "stock_price": 100
}

result = dividend_yield_calculator(inputs)
print(result)
