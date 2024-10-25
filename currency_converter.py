def currency_converter(inputs):
    """
    Converts an amount from one currency to another based on an exchange rate.

    Parameters:
    inputs (dict): A dictionary with the following keys:
        - 'amount' (float): The amount of money to convert.
        - 'exchange_rate' (float): Exchange rate from the base currency to the target currency.

    Returns:
    dict: A dictionary with the converted amount.
    """
    # Extract values from inputs
    amount = inputs.get('amount', 0)
    exchange_rate = inputs.get('exchange_rate', 1)
    
    # Calculate converted amount
    converted_amount = amount * exchange_rate

    # Output dictionary
    output = {
        "amount": amount,
        "exchange_rate": exchange_rate,
        "converted_amount": round(converted_amount, 2)
    }
    
    return output

# Example usage
inputs = {
    "amount": 100,
    "exchange_rate": 74.85  # Example rate for USD to INR
}

result = currency_converter(inputs)
print(result)
