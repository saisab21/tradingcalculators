def inflation_impact_calculator(inputs):
    """
    Calculates the future value of money adjusted for inflation.

    Parameters:
    inputs (dict): A dictionary with the following keys:
        - 'current_amount' (float): Current amount of money.
        - 'inflation_rate' (float): Annual inflation rate (percentage).
        - 'years' (int): Number of years in the future.

    Returns:
    dict: A dictionary with the adjusted future value and the reduction in purchasing power.
    """
    # Extract values from inputs
    current_amount = inputs.get('current_amount', 0)
    inflation_rate = inputs.get('inflation_rate', 0) / 100  # Convert percentage to decimal
    years = inputs.get('years', 0)
    
    # Calculate future value adjusted for inflation
    future_value = current_amount / ((1 + inflation_rate) ** years)
    purchasing_power_loss = current_amount - future_value

    # Output dictionary
    output = {
        "current_amount": current_amount,
        "inflation_rate": inputs.get('inflation_rate', 0),
        "years": years,
        "future_value_adjusted": round(future_value, 2),
        "purchasing_power_loss": round(purchasing_power_loss, 2)
    }
    
    return output

# Example usage
inputs = {
    "current_amount": 10000,
    "inflation_rate": 3,
    "years": 10
}

result = inflation_impact_calculator(inputs)
print(result)
