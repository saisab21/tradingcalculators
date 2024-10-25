def expected_rate_of_return_calculator(inputs):
    """
    Calculates the expected rate of return based on initial investment, future value, and investment duration.

    Parameters:
    inputs (dict): A dictionary with the following keys:
        - 'initial_investment' (float): Initial amount invested.
        - 'future_value' (float): Future value of the investment.
        - 'years' (int): Number of years the money was invested.

    Returns:
    dict: A dictionary with the calculated expected rate of return.
    """
    try:
        initial_investment = float(inputs.get('initial_investment', 0))
        future_value = float(inputs.get('future_value', 0))
        years = int(inputs.get('years', 0))

        if initial_investment <= 0 or future_value <= 0 or years <= 0:
            return {"error": "All input values must be positive."}

        rate_of_return = ((future_value / initial_investment) ** (1 / years) - 1) * 100

        return {
            "initial_investment": initial_investment,
            "future_value": future_value,
            "years": years,
            "rate_of_return": round(rate_of_return, 2)
        }

    except ValueError:
        return {"error": "Invalid input: Ensure all inputs are numbers."}
    except Exception as e:
        return {"error": f"An unexpected error occurred: {e}"}

# Example usage
inputs = {
    "initial_investment": 10000,
    "future_value": 20000,
    "years": 5
}

result = expected_rate_of_return_calculator(inputs)
print(result)
