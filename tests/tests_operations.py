import pytest
from utils import get_date, mask_from_to, get_filtered_and_sorted, mask_account, mask_card_number


def test_get_date():
    assert get_date("2018-08-14T05:42:30.104666") == "14.08.2018"
    assert get_date("2019-07-13T18:51:29.313309") == "13.07.2019"
    assert get_date("2018-12-22T02:02:49.564873") == "22.12.2018"
    assert get_date("2019-08-19T16:30:41.967497") == "19.08.2019"

def test_mask_from_to():
    assert mask_from_to("Счет 98841213648056852372") == "Счет **2372"
    assert mask_from_to("Счет 71687416928274675290") == "Счет **5290"
    assert mask_from_to("Visa Gold 8326537236216459") == "Visa Gold 8326 53** **** 6459"
    assert mask_from_to("МИР 3766446452238784") == "МИР 3766 44** **** 8784"
    assert mask_from_to("MasterCard 6783917276771847") == "MasterCard 6783 91** **** 1847"
    assert mask_from_to("Maestro 1308795367077170") == "Maestro 1308 79** **** 7170"

def test_get_filtered_and_sorted():
    assert (len(get_filtered_and_sorted([{"state": "EXECUTED"}, {"state": "CANCELED"}])) == 1)

def test_mask_account():
    assert mask_account("27804394774631586026") == "**6026"
    with pytest.raises(ValueError):
        assert mask_account("026")
    with pytest.raises(ValueError):
        assert mask_account("")

def test_mask_card_number():
    assert mask_card_number("6381702861749111") == "6381 70** **** 9111"
    with pytest.raises(ValueError):
        assert mask_card_number("63817061749111")
    with pytest.raises(ValueError):
        assert mask_card_number("")


