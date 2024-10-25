def inflation_impact_calculator(inputs):
    """
    Calculates the future value of money adjusted for inflation.

    Parameters:
    inputs (dict): A dictionary with the following keys:
        - 'current_amount' (float): Current amount of money.
        - 'inflation_rate' (float): Annual inflation rate (percentage).
        - 'years' (int): Number of years in the future.

    Returns:
    dict: A dictionary with the adjusted future value and the reduction in purchasing power or an error message.
    """
    try:
        current_amount = float(inputs.get('current_amount', 0))
        inflation_rate = float(inputs.get('inflation_rate', 0)) / 100
        years = int(inputs.get('years', 0))

        if current_amount < 0 or inflation_rate < 0 or years < 0:
            return {"error": "All input values must be non-negative."}

        future_value = current_amount / ((1 + inflation_rate) ** years)
        purchasing_power_loss = current_amount - future_value

        return {
            "current_amount": current_amount,
            "inflation_rate": inputs.get('inflation_rate', 0),
            "years": years,
            "future_value_adjusted": round(future_value, 2),
            "purchasing_power_loss": round(purchasing_power_loss, 2)
        }

    except ValueError:
        return {"error": "Invalid input: Ensure all inputs are numbers."}
    except Exception as e:
        return {"error": f"An unexpected error occurred: {e}"}

# Example usage
inputs = {
    "current_amount": 10000,
    "inflation_rate": 3,
    "years": 10
}

result = inflation_impact_calculator(inputs)
print(result)
