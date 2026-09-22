def main() -> None:
    while True:
        try:
            year: int = int(input("Enter the year: "))
        except ValueError:
            print("Error: Try again with a valid year.")
        else:
            if year % 400 == 0:
                print("Leap year.")
            elif year % 100 == 0:
                print("Not a leap year.")
            elif year % 4 == 0:
                print("Leap year.")
            else:
                print("Not a leap year.")
        if input("Do you want to continue? (y/n): ").lower() in ("n", "no", "т"):
            break


if __name__ == "__main__":
    main()
