def apply_discount(price, discount):
    if not isinstance(price, (int, float)):
        return("The price should be a number")

    if not isinstance(discount, (int, float)):
        return("The discount should be a number")

    if not price > 0:
        return ("The price should be greater than 0")

    if discount < 0 or discount > 100:
        return ("The discount should be between 0 and 100")

    return (price - (discount / 100) * price)

# Passed:7. apply_discount(100, 20) should return 80.
# Passed:8. apply_discount(200, 50) should return 100.
# Passed:9. apply_discount(50, 0) should return 50.
# Passed:11. apply_discount(74.5, 20.0) should return 59.6.
