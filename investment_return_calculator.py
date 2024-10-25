def investment_return_calculator(inputs):
    """
    Calculates the future value of an investment with regular annual contributions and a specified return rate.
    Error handling included for missing or invalid input values.

    Parameters:
    inputs (dict): A dictionary with the following keys:
        - 'initial_investment' (float): Initial amount invested.
        - 'annual_contribution' (float): Amount added every year.
        - 'rate_of_return' (float): Expected annual rate of return (in percentage).
        - 'years' (int): Number of years the money is invested.

    Returns:
    dict: A dictionary with details of the investment including the final value or an error message.
    """
    try:
        # Extract values from inputs with validation
        initial_investment = float(inputs.get('initial_investment', 0))
        annual_contribution = float(inputs.get('annual_contribution', 0))
        rate_of_return = float(inputs.get('rate_of_return', 0)) / 100  # Convert percentage to decimal
        years = int(inputs.get('years', 0))

        # Validate inputs
        if initial_investment < 0 or annual_contribution < 0 or rate_of_return < 0 or years < 0:
            return {"error": "All input values must be non-negative."}

        # Calculate future value
        future_value = initial_investment * (1 + rate_of_return) ** years
        for year in range(1, years + 1):
            future_value += annual_contribution * (1 + rate_of_return) ** (years - year)

        return {
            "initial_investment": initial_investment,
            "annual_contribution": annual_contribution,
            "rate_of_return": inputs.get('rate_of_return', 0),
            "years": years,
            "future_value": round(future_value, 2)
        }

    except ValueError:
        return {"error": "Invalid input: Ensure all inputs are numbers."}
    except Exception as e:
        return {"error": f"An unexpected error occurred: {e}"}

# Example usage
inputs = {
    "initial_investment": 10000,
    "annual_contribution": 2000,
    "rate_of_return": 7,
    "years": 10
}

result = investment_return_calculator(inputs)
print(result)
