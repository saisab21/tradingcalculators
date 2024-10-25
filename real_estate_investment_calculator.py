def real_estate_investment_calculator(inputs):
    """
    Calculates the annual return on a real estate investment.

    Parameters:
    inputs (dict): A dictionary with the following keys:
        - 'property_value' (float): Purchase price of the property.
        - 'annual_rental_income' (float): Annual income generated from renting the property.
        - 'annual_expenses' (float): Total annual expenses, including taxes, maintenance, and insurance.

    Returns:
    dict: A dictionary with the calculated return on investment or an error message.
    """
    try:
        property_value = float(inputs.get('property_value', 0))
        annual_rental_income = float(inputs.get('annual_rental_income', 0))
        annual_expenses = float(inputs.get('annual_expenses', 0))

        if property_value <= 0 or annual_rental_income < 0 or annual_expenses < 0:
            return {"error": "Property value must be positive, and income/expenses cannot be negative."}

        annual_net_income = annual_rental_income - annual_expenses
        roi = (annual_net_income / property_value) * 100

        return {
            "property_value": property_value,
            "annual_rental_income": annual_rental_income,
            "annual_expenses": annual_expenses,
            "annual_net_income": round(annual_net_income, 2),
            "roi": round(roi, 2)
        }

    except ValueError:
        return {"error": "Invalid input: Ensure all inputs are numbers."}
    except Exception as e:
        return {"error": f"An unexpected error occurred: {e}"}

# Example usage
inputs = {
    "property_value": 300000,
    "annual_rental_income": 24000,
    "annual_expenses": 5000
}

result = real_estate_investment_calculator(inputs)
print(result)
