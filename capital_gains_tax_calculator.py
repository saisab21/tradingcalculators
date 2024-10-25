def capital_gains_tax_calculator(inputs):
    """
    Calculates capital gains tax based on purchase and sale prices and holding period.

    Parameters:
    inputs (dict): A dictionary with the following keys:
        - 'purchase_price' (float): Price at which the asset was bought.
        - 'sale_price' (float): Price at which the asset was sold.
        - 'quantity' (int): Number of units sold.
        - 'holding_period' (int): Holding period in years.
        - 'tax_rate_short' (float): Short-term capital gains tax rate (percentage).
        - 'tax_rate_long' (float): Long-term capital gains tax rate (percentage).

    Returns:
    dict: A dictionary with calculated capital gain and applicable tax.
    """
    # Extract values from inputs
    purchase_price = inputs.get('purchase_price', 0)
    sale_price = inputs.get('sale_price', 0)
    quantity = inputs.get('quantity', 0)
    holding_period = inputs.get('holding_period', 0)
    tax_rate_short = inputs.get('tax_rate_short', 15) / 100  # Default rate
    tax_rate_long = inputs.get('tax_rate_long', 10) / 100  # Default rate
    
    # Calculate capital gain
    capital_gain = (sale_price - purchase_price) * quantity
    tax_rate = tax_rate_long if holding_period > 1 else tax_rate_short
    tax_due = capital_gain * tax_rate if capital_gain > 0 else 0

    # Output dictionary
    output = {
        "purchase_price": purchase_price,
        "sale_price": sale_price,
        "quantity": quantity,
        "holding_period": holding_period,
        "capital_gain": round(capital_gain, 2),
        "tax_due": round(tax_due, 2)
    }
    
    return output

# Example usage
inputs = {
    "purchase_price": 100,
    "sale_price": 150,
    "quantity": 50,
    "holding_period": 2,
    "tax_rate_short": 15,
    "tax_rate_long": 10
}

result = capital_gains_tax_calculator(inputs)
print(result)
