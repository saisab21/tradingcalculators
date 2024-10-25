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
    try:
        # Extract values from inputs with validation
        entry_price = float(inputs.get('entry_price', 0))
        exit_price = float(inputs.get('exit_price', 0))
        quantity = int(inputs.get('quantity', 0))

        if entry_price <= 0 or exit_price <= 0 or quantity <= 0:
            return {"error": "All input values must be positive and non-zero."}

        # Calculate profit or loss
        profit_loss = (exit_price - entry_price) * quantity

        return {
            "entry_price": entry_price,
            "exit_price": exit_price,
            "quantity": quantity,
            "profit_loss": round(profit_loss, 2)
        }

    except ValueError:
        return {"error": "Invalid input: Ensure all inputs are numbers."}
    except Exception as e:
        return {"error": f"An unexpected error occurred: {e}"}

# Example usage
inputs = {
    "entry_price": 100,
    "exit_price": 110,
    "quantity": 50
}

result = profit_loss_calculator(inputs)
print(result)
