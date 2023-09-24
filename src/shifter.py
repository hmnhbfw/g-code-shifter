from decimal import Decimal

from coordinates import PATTERN, Axis, Coordinates


class Shifter:
    shift_coords: Coordinates

    def __init__(self, shift_coords: Coordinates):
        self.shift_coords = shift_coords

    def process(self, from_file: str, to_file: str):
        with open(from_file, "r", encoding="utf-8") as input_file:
            with open(to_file, "a+", encoding="utf-8") as output_file:
                line: str = input_file.readline()
                while line:
                    output_line: str = ""
                    iterator = PATTERN.finditer(line)
                    coords = Coordinates()
                    pos = 0
                    for match in iterator:
                        start, end = match.span()
                        output_line += match.string[pos:start]
                        axis, coord  = coords.parse(match.string[start:end])
                        shifted_coord = self.shift(axis, coord)
                        output_line += axis.name + str(shifted_coord)
                        pos = end

                    output_line += line[pos:]
                    output_file.write(output_line)
                    line = input_file.readline()

                output_file.write("\n")

    def shift(self, axis: Axis, original: Decimal) -> Decimal:
        if axis is Axis.X and self.shift_coords.x is not None:
            return original + self.shift_coords.x
        if axis is Axis.Y and self.shift_coords.y is not None:
            return original + self.shift_coords.y
        if axis is Axis.Z and self.shift_coords.z is not None:
            return original + self.shift_coords.z
        return original
