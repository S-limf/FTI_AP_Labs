from typing import ClassVar


class MeasureUnit:
    all_units: ClassVar[list["MeasureUnit"]] = []

    def __init__(
        self, name: str, abbreviation: str, base_ratio: float
    ):  # base_ratio - коэффициент базового отношения к метру
        self.name = name
        self.abbreviation = abbreviation
        self.base_ratio = base_ratio
        MeasureUnit.all_units.append(self)

    def convert_to(self, target_unit: "MeasureUnit", value: float) -> float:
        return value * (self.base_ratio / target_unit.base_ratio)

    def __str__(self) -> str:
        abbreviation = f"({self.abbreviation})"
        return f"{self.name:<15}{abbreviation:>6}"

    @classmethod
    def get_all_units(cls) -> dict[str, "MeasureUnit"]:
        return {unit.abbreviation: unit for unit in cls.all_units}


def main() -> None:
    _kilometer: MeasureUnit = MeasureUnit("kilometer", "km", 1000.0)
    _meter: MeasureUnit = MeasureUnit("meter", "m", 1.0)
    _centimeter: MeasureUnit = MeasureUnit("centimeter", "cm", 0.01)
    _millimeter: MeasureUnit = MeasureUnit("millimeter", "mm", 0.001)
    _mile: MeasureUnit = MeasureUnit("mile", "mi", 1609.34)
    _yard: MeasureUnit = MeasureUnit("yard", "yd", 0.9144)

    units: dict[str, MeasureUnit] = MeasureUnit.get_all_units()

    while True:
        print(f"{'Available units':-^21}")
        for unit in units.values():
            print(unit)
        try:
            first_unit: str = str(input("Enter the unit to convert FROM: "))
            second_unit: str = str(input("Enter the unit to convert INTO: "))
            value: float = float(input("Enter the value: "))
            result: float = units[first_unit].convert_to(units[second_unit], value)
        except KeyError:
            print("Error: Try again with a valid unit.")
        except ValueError:
            print("Error: Invalid input. Please enter a numeric value.")
        else:
            print(f"{value} {first_unit} = {result} {second_unit}")
        if input("Continue? (y/n): ").lower() in ("n", "no", "т"):
            break


if __name__ == "__main__":
    main()
