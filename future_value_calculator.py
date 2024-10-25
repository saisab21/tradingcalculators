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
    try:
        initial_investment = float(inputs.get('initial_investment', 0))
        rate_of_return = float(inputs.get('rate_of_return', 0)) / 100
        years = int(inputs.get('years', 0))

        if initial_investment < 0 or rate_of_return < 0 or years < 0:
            return {"error": "All input values must be non-negative."}

        future_value = initial_investment * (1 + rate_of_return) ** years

        return {
            "initial_investment": initial_investment,
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
    "rate_of_return": 7,
    "years": 10
}

result = future_value_calculator(inputs)
print(result)
