def break_even_calculator(inputs):
    """
    Calculates the break-even point for a trade, including transaction fees.

    Parameters:
    inputs (dict): A dictionary with the following keys:
        - 'entry_price' (float): Price at which the stock was purchased.
        - 'quantity' (int): Number of shares purchased.
        - 'fees' (float): Total transaction fees (in currency).

    Returns:
    dict: A dictionary with the break-even price.
    """
    # Extract values from inputs
    entry_price = inputs.get('entry_price', 0)
    quantity = inputs.get('quantity', 0)
    fees = inputs.get('fees', 0)
    
    # Calculate break-even price
    break_even_price = (entry_price * quantity + fees) / quantity if quantity > 0 else 0

    # Output dictionary
    output = {
        "entry_price": entry_price,
        "quantity": quantity,
        "fees": fees,
        "break_even_price": round(break_even_price, 2)
    }
    
    return output

# Example usage
inputs = {
    "entry_price": 100,
    "quantity": 50,
    "fees": 20
}

result = break_even_calculator(inputs)
print(result)
