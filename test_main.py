import pytest
from transactions import mask_account, mask_card

def test_mask_account():
    assert mask_account("Счет 1234567890123456") == "**3456"

def test_mask_card():
    assert mask_card("Visa Platinum 7000 7900 1234 6361") == "Visa Platinum 7000 **** **** 6361"
