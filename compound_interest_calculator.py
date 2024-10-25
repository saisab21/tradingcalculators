def compound_interest_calculator(inputs):
    """
    Calculates the future value of an investment with compound interest.

    Parameters:
    inputs (dict): A dictionary with the following keys:
        - 'principal' (float): Initial amount invested.
        - 'rate' (float): Annual interest rate (percentage).
        - 'years' (int): Number of years the investment will grow.
        - 'compounds_per_year' (int): Number of times interest is compounded per year.

    Returns:
    dict: A dictionary with the calculated future value.
    """
    # Extract values from inputs
    principal = inputs.get('principal', 0)
    rate = inputs.get('rate', 0) / 100  # Convert percentage to decimal
    years = inputs.get('years', 0)
    compounds_per_year = inputs.get('compounds_per_year', 1)
    
    # Calculate compound interest
    future_value = principal * (1 + rate / compounds_per_year) ** (compounds_per_year * years)

    # Output dictionary
    output = {
        "principal": principal,
        "rate": inputs.get('rate', 0),
        "years": years,
        "compounds_per_year": compounds_per_year,
        "future_value": round(future_value, 2)
    }
    
    return output

# Example usage
inputs = {
    "principal": 10000,
    "rate": 5,
    "years": 10,
    "compounds_per_year": 4
}

result = compound_interest_calculator(inputs)
print(result)
