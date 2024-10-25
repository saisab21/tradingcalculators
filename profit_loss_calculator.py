def profit_loss_calculator(inputs):
    """
    Calculates the potential profit or loss for a trade based on entry and exit prices.

    Parameters:
    inputs (dict): A dictionary with the following keys:
        - 'entry_price' (float): Price at which the stock was purchased.
        - 'exit_price' (float): Price at which the stock is expected to be sold.
        - 'quantity' (int): Number of shares purchased.

    Returns:
    dict: A dictionary with details of the trade including profit or loss.
    """
    # Extract values from inputs
    entry_price = inputs.get('entry_price', 0)
    exit_price = inputs.get('exit_price', 0)
    quantity = inputs.get('quantity', 0)
    
    # Calculate profit or loss
    profit_loss = (exit_price - entry_price) * quantity

    # Output dictionary
    output = {
        "entry_price": entry_price,
        "exit_price": exit_price,
        "quantity": quantity,
        "profit_loss": round(profit_loss, 2)
    }
    
    return output

# Example usage
inputs = {
    "entry_price": 100,
    "exit_price": 110,
    "quantity": 50
}

result = profit_loss_calculator(inputs)
print(result)
