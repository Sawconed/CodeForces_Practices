import math


def max_dominoes(M: int, N: int) -> int:
    return math.floor(M * N / 2)


def main() -> None:
    M, N = (int(x) for x in input().split(' '))
    print(max_dominoes(M, N))


if __name__ == "__main__":
    main()
