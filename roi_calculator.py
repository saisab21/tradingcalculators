def roi_calculator(inputs):
    """
    Calculates the Return on Investment (ROI).

    Parameters:
    inputs (dict): A dictionary with the following keys:
        - 'initial_investment' (float): Initial amount invested.
        - 'final_value' (float): Final value of the investment.

    Returns:
    dict: A dictionary with the calculated ROI percentage or an error message.
    """
    try:
        initial_investment = float(inputs.get('initial_investment', 0))
        final_value = float(inputs.get('final_value', 0))

        if initial_investment <= 0 or final_value < 0:
            return {"error": "Initial investment must be positive, and final value cannot be negative."}

        roi = ((final_value - initial_investment) / initial_investment) * 100

        return {
            "initial_investment": initial_investment,
            "final_value": final_value,
            "roi": round(roi, 2)
        }

    except ValueError:
        return {"error": "Invalid input: Ensure all inputs are numbers."}
    except Exception as e:
        return {"error": f"An unexpected error occurred: {e}"}

# Example usage
inputs = {
    "initial_investment": 10000,
    "final_value": 15000
}

result = roi_calculator(inputs)
print(result)
