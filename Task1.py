class TriangleError(Exception):
    pass


def main() -> None:
    while True:
        try:
            a: float = float(input("Введите длину стороны a: "))
            b: float = float(input("Введите длину стороны b: "))
            c: float = float(input("Введите длину стороны c: "))
            if a + b <= c or a + c <= b or b + c <= a:
                raise TriangleError("Ошибка: Стороны не могут образовать треугольник")
        except ValueError:
            print("Ошибка: Введите числовое значение")
        except TriangleError as e:
            print(e)

        else:
            p: float = (a + b + c) / 2
            S: float = (p * (p - a) * (p - b) * (p - c)) ** 0.5
            print(f"Площадь: {S:.2f}")
            break


if __name__ == "__main__":
    main()
