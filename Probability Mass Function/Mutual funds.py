def calculate_cagr(initial_value, final_value, years):
    """
    Calculate the Compound Annual Growth Rate (CAGR).

    :param initial_value: The initial value of the investment.
    :param final_value: The final value of the investment.
    :param years: The number of years the investment was held.
    :return: The CAGR as a percentage.
    """
    cagr = (final_value / initial_value) ** (1 / years) - 1
    return cagr * 100

# Example usage
initial_investment = 12000  # Initial investment amount
final_investment = 130000    # Final investment amount
investment_years = 5        # Number of years

cagr = calculate_cagr(initial_investment, final_investment, investment_years)
print(f"The CAGR is {cagr:.2f}%")