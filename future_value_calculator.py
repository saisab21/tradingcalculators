def future_value_calculator(inputs):
    """
    Calculates the future value of a single investment based on the annual rate of return.

    Parameters:
    inputs (dict): A dictionary with the following keys:
        - 'initial_investment' (float): Initial amount invested.
        - 'rate_of_return' (float): Expected annual rate of return (percentage).
        - 'years' (int): Number of years the investment will grow.

    Returns:
    dict: A dictionary with the calculated future value.
    """
    # Extract values from inputs
    initial_investment = inputs.get('initial_investment', 0)
    rate_of_return = inputs.get('rate_of_return', 0) / 100  # Convert percentage to decimal
    years = inputs.get('years', 0)
    
    # Calculate future value
    future_value = initial_investment * (1 + rate_of_return) ** years

    # Output dictionary
    output = {
        "initial_investment": initial_investment,
        "rate_of_return": inputs.get('rate_of_return', 0),
        "years": years,
        "future_value": round(future_value, 2)
    }
    
    return output

# Example usage
inputs = {
    "initial_investment": 10000,
    "rate_of_return": 7,
    "years": 10
}

result = future_value_calculator(inputs)
print(result)
