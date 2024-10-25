def position_size_calculator(inputs):
    """
    Calculates the optimal position size based on risk tolerance, account size, and stop loss level.

    Parameters:
    inputs (dict): A dictionary with the following keys:
        - 'account_size' (float): Total size of the trading account.
        - 'risk_percentage' (float): Percentage of the account the user is willing to risk.
        - 'entry_price' (float): The price at which the trade will be entered.
        - 'stop_loss_price' (float): The price at which the trade will be exited if it moves against the trader.

    Returns:
    dict: A dictionary with details of the position size, including units to buy/sell and dollar risk.
    """
    try:
        # Extract and validate inputs
        account_size = float(inputs.get('account_size', 0))
        risk_percentage = float(inputs.get('risk_percentage', 0)) / 100  # Convert to decimal
        entry_price = float(inputs.get('entry_price', 0))
        stop_loss_price = float(inputs.get('stop_loss_price', 0))

        if account_size < 0 or risk_percentage < 0 or entry_price <= 0 or stop_loss_price <= 0:
            return {"error": "All input values must be positive and non-zero."}

        # Calculate risk per unit (difference between entry and stop loss)
        risk_per_unit = abs(entry_price - stop_loss_price)
        dollar_risk = account_size * risk_percentage

        # Calculate position size (number of units)
        position_size = dollar_risk / risk_per_unit if risk_per_unit > 0 else 0

        return {
            "account_size": account_size,
            "risk_percentage": inputs.get('risk_percentage', 0),
            "entry_price": entry_price,
            "stop_loss_price": stop_loss_price,
            "dollar_risk": round(dollar_risk, 2),
            "position_size": int(position_size)  # Rounded to whole units
        }

    except ValueError:
        return {"error": "Invalid input: Ensure all inputs are numbers."}
    except Exception as e:
        return {"error": f"An unexpected error occurred: {e}"}

# Example usage
inputs = {
    "account_size": 10000,
    "risk_percentage": 2,
    "entry_price": 50,
    "stop_loss_price": 47
}

result = position_size_calculator(inputs)
print(result)
