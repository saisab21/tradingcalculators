from forex_python.converter import CurrencyRates, CurrencyCodes

def currency_converter(inputs):
    """
    Converts an amount from one currency to another based on the live exchange rate using forex-python.

    Parameters:
    inputs (dict): A dictionary with the following keys:
        - 'amount' (float): The amount of money to convert.
        - 'base_currency' (str): Currency code for the base currency (e.g., 'USD').
        - 'target_currency' (str): Currency code for the target currency (e.g., 'INR').

    Returns:
    dict: A dictionary with the converted amount, exchange rate, and currency symbols, or an error message.
    """
    try:
        # Initialize forex-python currency converter
        c = CurrencyRates()
        cc = CurrencyCodes()

        # Extract and validate inputs
        amount = float(inputs.get('amount', 0))
        base_currency = inputs.get('base_currency', 'USD').upper()
        target_currency = inputs.get('target_currency', 'INR').upper()

        if amount < 0:
            return {"error": "Amount must be non-negative."}

        # Get the exchange rate and convert the amount
        exchange_rate = c.get_rate(base_currency, target_currency)
        converted_amount = c.convert(base_currency, target_currency, amount)

        # Get currency symbols
        base_symbol = cc.get_symbol(base_currency) or base_currency
        target_symbol = cc.get_symbol(target_currency) or target_currency

        return {
            "amount": f"{base_symbol} {amount}",
            "base_currency": base_currency,
            "target_currency": target_currency,
            "exchange_rate": round(exchange_rate, 4),
            "converted_amount": f"{target_symbol} {round(converted_amount, 2)}"
        }

    except ValueError:
        return {"error": "Invalid input: Ensure amount is a number."}
    except Exception as e:
        return {"error": f"An unexpected error occurred: {e}"}

# Example usage
inputs = {
    "amount": 100,
    "base_currency": "USD",
    "target_currency": "INR"
}

result = currency_converter(inputs)
print(result)
