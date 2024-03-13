def yearly_compare(a: int, b: int) -> int:
    year = 0

    while a <= b:
        a *= 3
        b *= 2
        year += 1

    return year


def main() -> None:
    a, b = (int(x) for x in input().split(' '))
    print(yearly_compare(a, b))


if __name__ == "__main__":
    main()
