def portfolio_rebalancing_calculator(inputs):
    """
    Calculates the amounts needed to rebalance a portfolio to match target allocations.

    Parameters:
    inputs (dict): A dictionary with the following keys:
        - 'current_allocations' (dict): Current allocations in each asset (e.g., {'Stocks': 5000, 'Bonds': 3000}).
        - 'target_allocations' (dict): Target allocation percentages (e.g., {'Stocks': 60, 'Bonds': 40}).

    Returns:
    dict: A dictionary with suggested rebalancing adjustments for each asset.
    """
    # Extract values from inputs
    current_allocations = inputs.get('current_allocations', {})
    target_allocations = inputs.get('target_allocations', {})
    
    # Calculate total current value
    total_current_value = sum(current_allocations.values())
    
    # Calculate target values based on target percentages
    rebalance_adjustments = {}
    for asset, current_value in current_allocations.items():
        target_percentage = target_allocations.get(asset, 0) / 100
        target_value = total_current_value * target_percentage
        adjustment = target_value - current_value
        rebalance_adjustments[asset] = round(adjustment, 2)

    # Output dictionary
    output = {
        "current_allocations": current_allocations,
        "target_allocations": target_allocations,
        "rebalance_adjustments": rebalance_adjustments
    }
    
    return output

# Example usage
inputs = {
    "current_allocations": {"Stocks": 7000, "Bonds": 3000},
    "target_allocations": {"Stocks": 60, "Bonds": 40}
}

result = portfolio_rebalancing_calculator(inputs)
print(result)
