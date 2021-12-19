from .constants import NOTHING
from .constants import SPACE
from .constants import SUPPORTED_ABBREVIATIONS


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
    parse_str = parse_str.strip()
    parse_str = parse_str.lower()
    parse_str = parse_str.replace(SPACE, NOTHING)
    multiplier = 0
    for multiplier_str, multiplier_int in SUPPORTED_ABBREVIATIONS:
        if multiplier_str in parse_str:
            parse_str = parse_str.replace(multiplier_str, NOTHING)
            multiplier = multiplier_int
            break
    frequency = int(parse_str) * multiplier
    return frequency
