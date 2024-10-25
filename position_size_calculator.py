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
    # Extract values from inputs
    account_size = inputs.get('account_size', 0)
    risk_percentage = inputs.get('risk_percentage', 0) / 100  # Convert percentage to decimal
    entry_price = inputs.get('entry_price', 0)
    stop_loss_price = inputs.get('stop_loss_price', 0)
    
    # Calculate risk per unit (difference between entry and stop loss)
    risk_per_unit = abs(entry_price - stop_loss_price)
    dollar_risk = account_size * risk_percentage  # Total dollar risk for the trade
    
    # Calculate position size (number of units)
    position_size = dollar_risk / risk_per_unit if risk_per_unit > 0 else 0

    # Output dictionary
    output = {
        "account_size": account_size,
        "risk_percentage": inputs.get('risk_percentage', 0),
        "entry_price": entry_price,
        "stop_loss_price": stop_loss_price,
        "dollar_risk": round(dollar_risk, 2),
        "position_size": int(position_size)  # Rounding to nearest whole unit
    }
    
    return output

# Example usage
inputs = {
    "account_size": 10000,
    "risk_percentage": 2,
    "entry_price": 50,
    "stop_loss_price": 47
}

result = position_size_calculator(inputs)
print(result)
