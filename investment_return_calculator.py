def investment_return_calculator(inputs):
    """
    Calculates the future value of an investment with regular annual contributions and a specified return rate.

    Parameters:
    inputs (dict): A dictionary with the following keys:
        - 'initial_investment' (float): Initial amount invested.
        - 'annual_contribution' (float): Amount added every year.
        - 'rate_of_return' (float): Expected annual rate of return (in percentage).
        - 'years' (int): Number of years the money is invested.

    Returns:
    dict: A dictionary with details of the investment including the final value.
    """
    # Extract values from inputs
    initial_investment = inputs.get('initial_investment', 0)
    annual_contribution = inputs.get('annual_contribution', 0)
    rate_of_return = inputs.get('rate_of_return', 0) / 100  # Convert percentage to decimal
    years = inputs.get('years', 0)
    
    # Calculate final amount
    future_value = initial_investment * (1 + rate_of_return) ** years
    for year in range(1, years + 1):
        future_value += annual_contribution * (1 + rate_of_return) ** (years - year)

    # Output dictionary
    output = {
        "initial_investment": initial_investment,
        "annual_contribution": annual_contribution,
        "rate_of_return": inputs.get('rate_of_return', 0),
        "years": years,
        "future_value": round(future_value, 2)
    }
    
    return output

# Example usage
inputs = {
    "initial_investment": 10000,
    "annual_contribution": 2000,
    "rate_of_return": 7,
    "years": 10
}

result = investment_return_calculator(inputs)
print(result)
