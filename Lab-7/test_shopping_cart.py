from hypothesis import given, strategies as st
from shopping_cart import cart_total, promo_percent, delivery_zone


# Test 1: Cart should not crash with unexpected inputs
@given(st.text() | st.none())
def test_cart_total_no_crash(s):
    result = cart_total(s)
    assert isinstance(result, int)
    assert result >= 0


# Test 2: Check total for correctly formatted cart items
@given(
    st.integers(min_value=0, max_value=1000),
    st.integers(min_value=0, max_value=100)
)
def test_cart_total_valid(price, qty):
    cart = f"pen:{price}x{qty}"
    assert cart_total(cart) == price * qty


# Test 3: Promo code should not crash with unexpected inputs
@given(st.text() | st.none())
def test_promo_percent_no_crash(s):
    result = promo_percent(s)
    assert isinstance(result, int)
    assert 0 <= result <= 100


# Test 4: Verify correctly formatted promo codes
@given(st.integers(min_value=0, max_value=100))
def test_promo_percent_valid(discount):
    code = f"OFF{discount}"
    assert promo_percent(code) == discount


# Test 5: Pincode should not crash with unexpected inputs
@given(st.text() | st.none())
def test_delivery_zone_no_crash(s):
    result = delivery_zone(s)
    assert isinstance(result, str)


# Test 6: Verify valid delivery zones
@given(st.sampled_from(list("12345678")))
def test_delivery_zone_valid(first_digit):
    pincode = first_digit + "00000"
    zones = {
        "1": "North", "2": "North",
        "3": "West", "4": "West",
        "5": "South", "6": "South",
        "7": "East", "8": "East"
    }
    assert delivery_zone(pincode) == zones[first_digit]
