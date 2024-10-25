def loan_emi_calculator(inputs):
    """
    Calculates the Equated Monthly Installment (EMI) for a loan.

    Parameters:
    inputs (dict): A dictionary with the following keys:
        - 'loan_amount' (float): Principal amount of the loan.
        - 'interest_rate' (float): Annual interest rate (percentage).
        - 'loan_tenure' (int): Loan tenure in years.

    Returns:
    dict: A dictionary with the calculated EMI amount.
    """
    # Extract values from inputs
    loan_amount = inputs.get('loan_amount', 0)
    interest_rate = inputs.get('interest_rate', 0) / 100 / 12  # Convert annual rate to monthly
    loan_tenure = inputs.get('loan_tenure', 0) * 12  # Convert years to months
    
    # EMI Calculation
    emi = (loan_amount * interest_rate * ((1 + interest_rate) ** loan_tenure)) / (((1 + interest_rate) ** loan_tenure) - 1)

    # Output dictionary
    output = {
        "loan_amount": loan_amount,
        "interest_rate": inputs.get('interest_rate', 0),
        "loan_tenure_years": inputs.get('loan_tenure', 0),
        "monthly_emi": round(emi, 2)
    }
    
    return output

# Example usage
inputs = {
    "loan_amount": 500000,
    "interest_rate": 7.5,
    "loan_tenure": 10
}

result = loan_emi_calculator(inputs)
print(result)
