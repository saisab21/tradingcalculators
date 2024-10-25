def loan_emi_calculator(inputs):
    """
    Calculates the Equated Monthly Installment (EMI) for a loan.

    Parameters:
    inputs (dict): A dictionary with the following keys:
        - 'loan_amount' (float): Principal amount of the loan.
        - 'interest_rate' (float): Annual interest rate (percentage).
        - 'loan_tenure' (int): Loan tenure in years.

    Returns:
    dict: A dictionary with the calculated EMI amount or an error message.
    """
    try:
        loan_amount = float(inputs.get('loan_amount', 0))
        interest_rate = float(inputs.get('interest_rate', 0)) / 100 / 12  # Monthly rate
        loan_tenure = int(inputs.get('loan_tenure', 0)) * 12  # Tenure in months

        if loan_amount <= 0 or interest_rate < 0 or loan_tenure <= 0:
            return {"error": "Loan amount and tenure must be positive. Interest rate must be non-negative."}

        emi = (loan_amount * interest_rate * ((1 + interest_rate) ** loan_tenure)) / (((1 + interest_rate) ** loan_tenure) - 1)

        return {
            "loan_amount": loan_amount,
            "interest_rate": inputs.get('interest_rate', 0),
            "loan_tenure_years": inputs.get('loan_tenure', 0),
            "monthly_emi": round(emi, 2)
        }

    except ValueError:
        return {"error": "Invalid input: Ensure all inputs are numbers."}
    except Exception as e:
        return {"error": f"An unexpected error occurred: {e}"}

# Example usage
inputs = {
    "loan_amount": 500000,
    "interest_rate": 7.5,
    "loan_tenure": 10
}

result = loan_emi_calculator(inputs)
print(result)
