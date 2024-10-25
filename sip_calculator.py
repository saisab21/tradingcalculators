def sip_calculator(inputs):
    """
    Calculates the future value of a Systematic Investment Plan (SIP) with regular contributions
    and a specified rate of return compounded monthly.

    Parameters:
    inputs (dict): A dictionary with the following keys:
        - 'monthly_investment' (float): The amount invested every month.
        - 'rate_of_return' (float): Expected annual rate of return (in percentage).
        - 'years' (int): Number of years the SIP is invested.

    Returns:
    dict: A dictionary with details of the SIP including the future value.
    """
    # Extract values from inputs
    monthly_investment = inputs.get('monthly_investment', 0)
    rate_of_return = inputs.get('rate_of_return', 0) / 100  # Convert percentage to decimal
    years = inputs.get('years', 0)
    
    # Convert annual rate to monthly rate
    monthly_rate = rate_of_return / 12
    total_months = years * 12
    
    # Future value calculation for SIP
    future_value = monthly_investment * (((1 + monthly_rate) ** total_months - 1) / monthly_rate) * (1 + monthly_rate)

    # Output dictionary
    output = {
        "monthly_investment": monthly_investment,
        "rate_of_return": inputs.get('rate_of_return', 0),
        "years": years,
        "future_value": round(future_value, 2)
    }
    
    return output

# Example usage
inputs = {
    "monthly_investment": 2000,
    "rate_of_return": 12,
    "years": 10
}

result = sip_calculator(inputs)
print(result)
