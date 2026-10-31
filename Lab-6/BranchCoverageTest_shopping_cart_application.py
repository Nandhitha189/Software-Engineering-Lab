
import pytest
from shopping_cart import item_total, cart_discount, shipping_fee


# ==========================================
# TEST CASES FOR ITEM TOTAL
# ==========================================

def test_food_item():
    assert item_total("food", 100, 2) == 210


def test_electronics_item():
    assert item_total("electronics", 1000, 1) == 1180


def test_clothing_item():
    assert item_total("clothing", 500, 2) == 1120


def test_bulk_discount():
    assert item_total("food", 100, 10) == 945


def test_no_bulk_discount():
    assert item_total("food", 100, 9) == 945


def test_invalid_category():
    with pytest.raises(ValueError):
        item_total("books", 100, 2)


def test_negative_price():
    with pytest.raises(ValueError):
        item_total("food", -100, 2)


def test_zero_quantity():
    with pytest.raises(ValueError):
        item_total("food", 100, 0)


def test_negative_quantity():
    with pytest.raises(ValueError):
        item_total("food", 100, -1)


# ==========================================
# TEST CASES FOR CART DISCOUNT
# ==========================================

def test_high_cart_discount():
    assert cart_discount(5000, False, None) == 500


def test_medium_cart_discount():
    assert cart_discount(2000, False, None) == 200


def test_no_cart_discount():
    assert cart_discount(999, False, None) == 0


def test_prime_discount():
    assert cart_discount(500, True, None) == 100


def test_valid_coupon():
    assert cart_discount(1000, False, "FLAT10") == 100


def test_coupon_below_minimum():
    assert cart_discount(999, False, "FLAT10") == 0


def test_invalid_coupon():
    assert cart_discount(1000, False, "INVALID") == 0


def test_combined_discount():
    assert cart_discount(5000, True, "FLAT10") == 1100


# ==========================================
# TEST CASES FOR SHIPPING FEE
# ==========================================

def test_free_shipping():
    assert shipping_fee(1000, False, False) == 0


def test_standard_shipping():
    assert shipping_fee(100, False, False) == 40


def test_prime_free_shipping():
    assert shipping_fee(100, True, False) == 0


def test_express_shipping():
    assert shipping_fee(100, False, True) == 140


def test_express_free_shipping():
    assert shipping_fee(500, False, True) == 100


def test_prime_express_shipping():
    assert shipping_fee(100, True, True) == 50
