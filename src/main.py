import os
import sys

from decimal import Decimal, getcontext

from shifter import Shifter, Coordinates


getcontext().prec = 5

def main():
    _, src_path, dst_path, count, *args = sys.argv

    if len(sys.argv) - 1 > 6:
        print("Passed more than six arguments", file=sys.stderr)

    if not os.path.isfile(src_path):
        print(f"File {src_path} is not found\n", file=sys.stderr)
        sys.exit(1)

    coords = Coordinates()
    for arg in args:
        coords.parse(arg)

    if count == "-":
        shifter = Shifter(coords)
        shifter.process(src_path, dst_path)
    else:
        try:
            for i in range(int(count)):
                next_coords = Coordinates(
                    coords.x * Decimal(i) if coords.x is not None else None,
                    coords.y * Decimal(i) if coords.y is not None else None,
                    coords.z * Decimal(i) if coords.z is not None else None)
                shifter = Shifter(next_coords)
                shifter.process(src_path, dst_path)
        except ValueError:
            print("The second argument 'count' must be either '-' or an integer.\n"
                  f"But given: '{count}'.",
                  file=sys.stderr)


if __name__ == "__main__":
    main()
