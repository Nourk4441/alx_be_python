def safe_divide(numerator, denominator):
    try:
        # Attempt to convert both inputs to float
        numerator = float(numerator)
        denominator = float(denominator)

        # Perform division, handling division by zero
        result = numerator / denominator
        return f"The result of the division is {result:.1f}"
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
    except ValueError:
        return "Error: Please enter numeric values only."
