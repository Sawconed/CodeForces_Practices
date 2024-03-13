def isDivisible(num: int) -> bool:
    return (num % 2 == 0) and (num > 3)


def main() -> None:
    num = int(input())
    print('YES' if isDivisible(num) else 'NO')


if __name__ == "__main__":
    main()
