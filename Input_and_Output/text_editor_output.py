def greeting():
    print("Hi there")


def calculate_pi():
    """
    Calculate pi to the 5th decimal digit using the Leibniz formula.
    Returns pi rounded to 5 decimal places (3.14159).
    """
    # Using a more efficient method: Machin's formula
    # pi/4 = 4*arctan(1/5) - arctan(1/239)
    
    def arctan(x, num_terms=500):
        """Calculate arctan using Taylor series"""
        result = 0
        for n in range(num_terms):
            sign = (-1) ** n
            result += sign * (x ** (2 * n + 1)) / (2 * n + 1)
        return result
    
    pi = 4 * (4 * arctan(1/5) - arctan(1/239))
    return round(pi, 5)
