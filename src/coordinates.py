import enum
import re
import sys

from decimal import Decimal


STR_PATTERN = r"[XYZ][+-]?(\d*\.\d+|\d+)"
PATTERN = re.compile(STR_PATTERN, re.IGNORECASE)


@enum.unique
class Axis(enum.Enum):
    X = "X"
    Y = "Y"
    Z = "Z"


class Coordinates:
    x: Decimal = None
    y: Decimal = None
    z: Decimal = None

    def __iter__(self):
        return iter((self.x, self.y, self.z))

    def parse(self, string: str) -> tuple[Axis, Decimal]:
        match = PATTERN.fullmatch(string)

        if match is None:
            Coordinates.print_error_format(string)
            sys.exit(1)

        first: str = match.string[0]
        if first in ("X", "x"):
            self.x = Decimal(match.string[1:])
            return Axis.X, self.x
        if first in ("Y", "y"):
            self.y = Decimal(match.string[1:])
            return Axis.Y, self.y
        if first in ("Z", "z"):
            self.z = Decimal(match.string[1:])
            return Axis.Z, self.z

    @staticmethod
    def print_error_format(text: str):
        print(
            f"Expected a string with the {STR_PATTERN} pattern.\nGot instead: {text}",
            file=sys.stderr
        )
