def portfolio_rebalancing_calculator(inputs):
    """
    Calculates the amounts needed to rebalance a portfolio to match target allocations.

    Parameters:
    inputs (dict): A dictionary with the following keys:
        - 'current_allocations' (dict): Current allocations in each asset (e.g., {'Stocks': 5000, 'Bonds': 3000}).
        - 'target_allocations' (dict): Target allocation percentages (e.g., {'Stocks': 60, 'Bonds': 40}).

    Returns:
    dict: A dictionary with suggested rebalancing adjustments for each asset or an error message.
    """
    try:
        current_allocations = inputs.get('current_allocations', {})
        target_allocations = inputs.get('target_allocations', {})

        if not current_allocations or not target_allocations:
            return {"error": "Both current and target allocations must be provided."}

        total_current_value = sum(current_allocations.values())

        rebalance_adjustments = {}
        for asset, current_value in current_allocations.items():
            if asset not in target_allocations:
                continue
            target_percentage = target_allocations[asset] / 100
            target_value = total_current_value * target_percentage
            adjustment = target_value - current_value
            rebalance_adjustments[asset] = round(adjustment, 2)

        return {
            "current_allocations": current_allocations,
            "target_allocations": target_allocations,
            "rebalance_adjustments": rebalance_adjustments
        }

    except Exception as e:
        return {"error": f"An unexpected error occurred: {e}"}

# Example usage
inputs = {
    "current_allocations": {"Stocks": 7000, "Bonds": 3000},
    "target_allocations": {"Stocks": 60, "Bonds": 40}
}

result = portfolio_rebalancing_calculator(inputs)
print(result)
