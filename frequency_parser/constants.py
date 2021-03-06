SPACE: str = " "
NOTHING: str = ""
DOT: str = "."
COMMA: str = ","
HZ: str = "hz"
KHZ: str = "khz"
MHZ: str = "mhz"
GHZ: str = "ghz"
THZ: str = "thz"

SUPPORTED_ABBREVIATIONS: list = [
    HZ,
    KHZ,
    MHZ,
    GHZ,
    THZ,
]

KHZ_MULTIPLIER: int = 1000
MHZ_MULTIPLIER: int = 1000000
GHZ_MULTIPLIER: int = 1000000000
THZ_MULTIPLIER: int = 1000000000000

SUPPORTED_ABBREVIATIONS: dict = {
    KHZ: KHZ_MULTIPLIER,
    MHZ: MHZ_MULTIPLIER,
    GHZ: GHZ_MULTIPLIER,
    THZ: THZ_MULTIPLIER,
}
