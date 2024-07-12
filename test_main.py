import pytest
from main import mask_card, mask_account

def test_mask_card():
    assert mask_card('1234567890123456') == 'XXXX XXXX XXXX 3456'

def test_mask_account():
    assert mask_account('123456789012') == '**** 9012'
