import math


def minimum_flagstones(n: int, m: int, a: int) -> int:
    return math.ceil(n/a) * math.ceil(m/a)


def main() -> None:
    n, m, a = (int(x) for x in input().split(' '))
    print(minimum_flagstones(n, m, a))


if __name__ == "__main__":
    main()
