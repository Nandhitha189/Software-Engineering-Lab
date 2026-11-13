import re

ZONES = {
    "1": "North", "2": "North",
    "3": "West", "4": "West",
    "5": "South", "6": "South",
    "7": "East", "8": "East"
}


def cart_total(cart):
    if not isinstance(cart, str) or not cart.strip():
        return 0

    total = 0

    for item in cart.split(","):
        parts = item.split(":")

        if len(parts) != 2 or not parts[0].strip():
            return 0

        price_qty = parts[1].split("x")

        if len(price_qty) != 2:
            return 0

        price, qty = price_qty

        if not re.fullmatch(r"[0-9]+", price.strip()):
            return 0

        if not re.fullmatch(r"[0-9]+", qty.strip()):
            return 0

        try:
            price = int(price.strip())
            qty = int(qty.strip())
        except ValueError:
            return 0

        total += price * qty

    return total


def promo_percent(code):
    if not isinstance(code, str):
        return 0

    match = re.fullmatch(r"OFF([0-9]{1,3})", code.strip(), re.I)

    if not match:
        return 0

    discount = int(match.group(1))

    if discount > 100:
        return 0

    return discount


def delivery_zone(pincode):
    if not isinstance(pincode, str):
        return "Unknown"

    pincode = pincode.strip()

    if not re.fullmatch(r"[0-9]{6}", pincode):
        return "Unknown"

    return ZONES.get(pincode[0], "Unknown")


def main():
    print("==== Running cart_total ====")
    user_input = input(
        "Enter cart as name:pricexqty CSV "
        "(e.g. pen:10x2,book:250x1): "
    )
    result = cart_total(user_input)
    print("Cart Total:", result)

    print("\n==== Running promo_percent ====")
    user_input = input("Enter a promo code (e.g. OFF20): ")
    result = promo_percent(user_input)
    print("Discount Percent:", result)

    print("\n==== Running delivery_zone ====")
    user_input = input(
        "Enter a 6 digit pincode (e.g. 560085): "
    )
    result = delivery_zone(user_input)
    print("Delivery Zone:", result)


if __name__ == "__main__":
    main()
