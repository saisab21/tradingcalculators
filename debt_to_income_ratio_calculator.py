def debt_to_income_ratio_calculator(inputs):
    """
    Calculates the debt-to-income (DTI) ratio.

    Parameters:
    inputs (dict): A dictionary with the following keys:
        - 'monthly_debt_payments' (float): Total monthly debt payments.
        - 'monthly_income' (float): Total monthly income.

    Returns:
    dict: A dictionary with the calculated DTI ratio or an error message.
    """
    try:
        monthly_debt_payments = float(inputs.get('monthly_debt_payments', 0))
        monthly_income = float(inputs.get('monthly_income', 0))

        if monthly_income <= 0:
            return {"error": "Monthly income must be positive."}

        dti_ratio = (monthly_debt_payments / monthly_income) * 100

        return {
            "monthly_debt_payments": monthly_debt_payments,
            "monthly_income": monthly_income,
            "dti_ratio": round(dti_ratio, 2)
        }

    except ValueError:
        return {"error": "Invalid input: Ensure all inputs are numbers."}
    except Exception as e:
        return {"error": f"An unexpected error occurred: {e}"}

# Example usage
inputs = {
    "monthly_debt_payments": 500,
    "monthly_income": 3000
}

result = debt_to_income_ratio_calculator(inputs)
print(result)
