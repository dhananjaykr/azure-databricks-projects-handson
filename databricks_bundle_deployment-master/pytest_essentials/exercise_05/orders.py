def calculate_discount(amount):
    if amount < 0:
        raise ValueError("Amount cannot be negative")

    if amount >= 10000:
        return amount * 0.10

    if amount >= 5000:
        return amount * 0.05

    return 0
