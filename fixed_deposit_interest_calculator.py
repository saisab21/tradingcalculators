def fixed_deposit_interest_calculator(inputs):
    """
    Calculates the maturity value of a fixed deposit with compounding interest.

    Parameters:
    inputs (dict): A dictionary with the following keys:
        - 'principal' (float): Principal amount deposited.
        - 'rate_of_interest' (float): Annual interest rate (percentage).
        - 'years' (int): Number of years the deposit is held.
        - 'compounds_per_year' (int): Number of times interest is compounded per year.

    Returns:
    dict: A dictionary with the maturity value or an error message.
    """
    try:
        principal = float(inputs.get('principal', 0))
        rate_of_interest = float(inputs.get('rate_of_interest', 0)) / 100
        years = int(inputs.get('years', 0))
        compounds_per_year = int(inputs.get('compounds_per_year', 1))

        if principal < 0 or rate_of_interest < 0 or years <= 0 or compounds_per_year <= 0:
            return {"error": "All inputs must be non-negative, and years/compounds must be positive."}

        maturity_value = principal * (1 + rate_of_interest / compounds_per_year) ** (compounds_per_year * years)

        return {
            "principal": principal,
            "rate_of_interest": inputs.get('rate_of_interest', 0),
            "years": years,
            "compounds_per_year": compounds_per_year,
            "maturity_value": round(maturity_value, 2)
        }

    except ValueError:
        return {"error": "Invalid input: Ensure all inputs are numbers."}
    except Exception as e:
        return {"error": f"An unexpected error occurred: {e}"}

# Example usage
inputs = {
    "principal": 50000,
    "rate_of_interest": 6.5,
    "years": 5,
    "compounds_per_year": 4
}

result = fixed_deposit_interest_calculator(inputs)
print(result)
