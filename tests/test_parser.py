import pytest

import frequency_parser

first_test_data = [
    ("100", 100),
    ("100,10", None),
    ("100.00", 100),
    ("200hz", 200),
    ("256HZ", 256),
    ("333khz", 333000),
    ("345kHz", 345000),
    ("355 KHZ", 355000),
    ("345.2111 khz", 345211),
    ("354,123khz", 354123),
    ("1Mhz", 1000000),
    ("1 Mhz", 1000000),
]


@pytest.mark.parametrize("fr, result", first_test_data)
def test_parser(fr, result):
    hz_value = frequency_parser.parse(test_parser)
    assert hz_value == result
