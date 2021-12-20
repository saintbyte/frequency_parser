from decimal import Decimal

from .constants import COMMA
from .constants import DOT
from .constants import HZ
from .constants import NOTHING
from .constants import SPACE
from .constants import SUPPORTED_ABBREVIATIONS


def _normalize_frequency(parse_str: str) -> str:
    parse_str = parse_str.strip()
    parse_str = parse_str.lower()
    parse_str = parse_str.replace(SPACE, NOTHING)
    parse_str = parse_str.replace(COMMA, DOT)
    return parse_str


def parse(parse_str: str) -> int:
    """
    Parse string with frequency and
    return frequency as int in hz
    Input:
        frequency as string
    Result:
        frequency in hz as int
    """
    frequency = 0
    if not isinstance(parse_str, str):
        ValueError("Must input string")
    parse_str = _normalize_frequency(parse_str)
    multiplier = 1
    for multiplier_str, multiplier_int in SUPPORTED_ABBREVIATIONS.items():
        if multiplier_str in parse_str:
            parse_str = parse_str.replace(multiplier_str, NOTHING)
            multiplier = multiplier_int
            break
    parse_str = parse_str.replace(HZ, NOTHING)
    frequency = int(Decimal(parse_str) * multiplier)
    return frequency
